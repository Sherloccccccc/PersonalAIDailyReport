# Daily Workflow

## Production Trigger

Use GitHub Actions.

Schedule:

```yaml
cron: "30 1 * * *"
```

This runs at 09:30 Asia/Shanghai.

Manual trigger is also available through `workflow_dispatch`.

## Required GitHub Secrets

| Secret | Required | Description |
|---|---:|---|
| `LARK_APP_ID` | yes | Feishu app id |
| `LARK_APP_SECRET` | yes | Feishu app secret |
| `FEISHU_CHAT_ID` | yes | Target chat id, usually `oc_...` |

Local `lark-cli` config showed app id:

```text
cli_a96cf46a56789bb5
```

Use it for `LARK_APP_ID` only if this is the Feishu app that should send the report.

## Daily Artifact Layout

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

## Daily Prompt

```text
Generate and send today's Daily AI Info.

Run date: today in Asia/Shanghai.

Workflow:
1. Pull the latest repository state.
2. Build the digest:
   - News source: Juya RSS
   - Paper source: arXiv API
   - arXiv RSS fallback enabled
   - paper state: data/paper-state.json
   - run directory: runs/YYYY-MM-DD
3. Generate:
   - runs/YYYY-MM-DD/daily-ai-info.md
   - runs/YYYY-MM-DD/digest-data.json
   - runs/YYYY-MM-DD/run-log.json
4. Send runs/YYYY-MM-DD/daily-ai-info.md to Feishu.
5. Update runs/YYYY-MM-DD/run-log.json with delivery status and message ids.
6. Update runs/index.jsonl with one row for this run.
7. Commit and push:
   - data/paper-state.json
   - runs/YYYY-MM-DD/
   - runs/index.jsonl

Acceptance:
- build command exits 0
- News count > 0
- Paper section exists
- delivery status is success
- run-log.json contains delivery.message_ids or a recorded delivery result
- committed artifacts are pushed to GitHub

Final response:
- run_id
- News count
- Paper selected count
- delivery status
- commit hash
- paths to daily-ai-info.md and run-log.json

Report rules:
- Do not include internal stats in daily-ai-info.md.
- News fields: title, 摘要, Original Link.
- Paper fields: title, Publish Date, 一句话总结, Link.
- GitHub artifact daily-ai-info.md stays standard Markdown.
- Feishu card body must be Feishu-safe: do not render `#`, `##`, or `###` as body text; convert section headings to bold plain lines instead.
- Feishu card body may use only bold text, numbered items, links, short paragraphs, and separators.
- Paper 一句话总结 should be around 80-120 Chinese characters and say what the paper specifically did.
- Paper 一句话总结 must be Chinese, not copied English from the abstract.
- Paper 一句话总结 should include at least two concrete elements when available: problem/object, method/framework, data/evaluation, result/use.
- Paper 一句话总结 must avoid generic filler like “围绕……展开”, “提供新方法、评测或工程线索”, and “核心贡献是：We introduce...”.
```

## Local Manual Run

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

Send:

```bash
python personal-ai-daily-report/scripts/send_lark_markdown.py \
  --markdown-file "runs/$RUN_ID/daily-ai-info.md" \
  --chat-id "$FEISHU_CHAT_ID" \
  --delivery-log "runs/$RUN_ID/run-log.json" \
  --result-json "runs/$RUN_ID/delivery-result.json"
```

Update index:

```bash
python - <<'PY'
import json
import os
from pathlib import Path

run_id = os.environ["RUN_ID"]
run_log_path = Path("runs") / run_id / "run-log.json"
run_log = json.loads(run_log_path.read_text(encoding="utf-8"))
row = {
    "run_id": run_id,
    "status": run_log.get("delivery", {}).get("status", "unknown"),
    "news_count": run_log.get("news_count"),
    "paper_selected_count": run_log.get("paper_selected_count"),
    "path": str(run_log_path),
    "generated_at": run_log.get("generated_at"),
    "sent_at": run_log.get("delivery", {}).get("sent_at"),
}
index_path = Path("runs/index.jsonl")
existing = []
if index_path.exists():
    existing = [
        json.loads(line)
        for line in index_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
existing = [item for item in existing if item.get("run_id") != run_id]
existing.append(row)
index_path.write_text(
    "\n".join(json.dumps(item, ensure_ascii=False) for item in existing) + "\n",
    encoding="utf-8",
)
PY
```
