---
name: personal-ai-daily-report
description: Build and deliver the user's Daily AI Info report. News comes from Juya RSS, Paper comes from arXiv with scoring, persistent paper state, Feishu delivery, and Git-backed run artifacts.
---

# Personal AI Daily Report

Use this skill to produce and deliver `Daily AI Info`.

## Stable Daily Workflow

The production path is GitHub Actions:

```text
GitHub Actions cron -> build digest -> send Feishu -> write run artifacts -> commit/push
```

Manual local build:

```bash
RUN_ID=$(TZ=Asia/Shanghai date +%F)
mkdir -p "runs/$RUN_ID" data
python personal-ai-daily-report/scripts/build_digest.py \
  --output-dir "runs/$RUN_ID" \
  --state-file data/paper-state.json \
  --run-summary "runs/$RUN_ID/run-log.json" \
  --run-id "$RUN_ID" \
  --top-k 10
```

Manual Feishu send:

```bash
python personal-ai-daily-report/scripts/send_lark_markdown.py \
  --markdown-file "runs/$RUN_ID/daily-ai-info.md" \
  --chat-id "$FEISHU_CHAT_ID" \
  --delivery-log "runs/$RUN_ID/run-log.json" \
  --result-json "runs/$RUN_ID/delivery-result.json"
```

## Sources

`News`:

- source: `https://imjuya.github.io/juya-ai-daily/rss.xml`
- parser: latest RSS item `content:encoded`
- keeps Juya categories such as `要闻`, `模型发布`, `开发生态`, `产品应用`, `技术与洞察`, `行业动态`, `前瞻与传闻`

`Paper`:

- primary source: arXiv API
- fallback source: arXiv RSS category feeds
- allowed arXiv categories: `cs.LG`, `cs.CL`, `cs.SE`
- blacklist terms: `clinical`, `psychiatric`, `lung cancer`, `biomechanical`, `traffic`, `driving`, `emboli`, `field medicine`, `legal`, `graph`

## Persistent Artifacts

```text
data/
  paper-state.json

runs/
  index.jsonl
  YYYY-MM-DD/
    daily-ai-info.md
    digest-data.json
    run-log.json
    delivery-result.json
```

`data/paper-state.json` is the long-lived paper table:

- stores scored paper candidates with full abstract
- `if_pushed = 0` means waiting list
- `if_pushed = 1` means already sent

`runs/YYYY-MM-DD/daily-ai-info.md` is the exact report body to send.

`runs/YYYY-MM-DD/digest-data.json` stores build internals: Juya issue, parsed news, paper candidates, dropped papers, selected papers, scores, and logs.

`runs/YYYY-MM-DD/run-log.json` stores the daily status and delivery result.

`runs/index.jsonl` stores one compact index row per run.

## Output Contract

Title:

```md
# Daily AI Info
```

Use only these top-level sections:

- `News`
- `Paper`

For each News item:

```md
1. **Title**

**摘要:**
Chinese summary.

**Original Link:**
https://...
```

For each Paper item:

```md
1. **Paper Title**

**Publish Date:**
YYYY-MM-DD

**一句话总结:**
Around 80-120 Chinese characters in Chinese, describing what the paper specifically did.

**Link:**
https://arxiv.org/abs/...
```

Do not include internal stats, candidate counts, delivery notes, scoring details, or build logs in `daily-ai-info.md`.

Feishu card delivery uses a safer subset than `daily-ai-info.md`: convert `#`, `##`, and `###` headings to bold plain lines before sending, because Feishu interactive cards do not reliably render Markdown heading syntax inside `lark_md`.

## Paper Scoring

The build script uses four 25-point dimensions:

- `application_relevance`
- `new_signal`
- `engineering_utility`
- `timeliness_rarity`

Keep selected papers at `top-k = 10` when available. If fewer papers pass threshold, send fewer. Waiting-list papers are selected by score without age decay.

Paper summaries must be concrete. Avoid generic filler such as:

- `围绕...展开`
- `核心贡献是：We introduce...`
- `工程线索`
- `新方法、评测或工程线索`

## Required Secrets For GitHub Actions

- `LARK_APP_ID`
- `LARK_APP_SECRET`
- `FEISHU_CHAT_ID`

The local `lark-cli` config showed app id `cli_a96cf46a56789bb5`; store that as `LARK_APP_ID` if this is the app you want the workflow to use. Do not commit app secrets.

## Windows UTF-8 Handling

For Chinese output, Chinese paths, or Feishu delivery on Windows, set UTF-8 first:

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
```

## Resources

- `scripts/build_digest.py`: builds report data, markdown, paper state, and run summary
- `scripts/send_lark_markdown.py`: sends markdown to Feishu and updates delivery status
- `references/selection-notes.md`: paper scoring and filtering notes
- `DAILY_WORKFLOW.md`: stable production workflow and daily prompt
