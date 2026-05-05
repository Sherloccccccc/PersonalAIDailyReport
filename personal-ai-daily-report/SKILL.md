---
name: personal-ai-daily-report
description: Build and deliver a personal daily AI digest from the Folo category "AI FrontEnd". Use when Codex needs to fetch recent Folo entries, keep all non-paper items as News, filter arXiv AI papers with fixed rules, select 10 papers balancing new signals and core themes, write a final markdown report, and optionally send it to Feishu/Lark chat.
---

# Personal AI Daily Report

Use this skill to produce the user's `Daily AI Info` report from Folo and deliver it to Feishu.

Keep the workflow deterministic until paper selection:

- use `scripts/build_digest.py` to fetch, paginate, split, filter, and enrich items
- use Codex judgment only for final paper selection and Chinese insights
- use `scripts/send_lark_markdown.py` for Feishu delivery to avoid Windows Unicode corruption

## Workflow

1. Run the build script from this skill directory:

```powershell
python scripts/build_digest.py --category "AI FrontEnd" --hours 24 --output-dir ".tmp/folo-daily"
```

2. Read `.tmp/folo-daily/digest-data.json` and `.tmp/folo-daily/digest-scaffold.md`.

3. Render all `news` entries in the final `News` section.

4. From `paper_candidates`, select 10 papers total when available:

- prefer 5 `new` signal papers
- prefer 5 `classic` or core-theme papers
- backfill from the other bucket only when the requested output allows it

5. Write the final markdown to the requested path. If no path is given, use:

```text
.tmp/folo-daily/daily-ai-info-final.md
```

6. If the user asks for delivery, send the prepared markdown:

```powershell
python scripts/send_lark_markdown.py --markdown-file ".tmp/folo-daily/daily-ai-info-final.md" --chat-id <chat_id>
```

If no `--chat-id` or `--user-id` is provided, the sender script resolves the current authenticated Feishu user via `lark-cli`.

## Output Contract

Title the report exactly:

```text
Daily AI Info
```

Use these sections:

- `News`
- `Paper`

For `News`:

- include every non-paper item
- number from 1 inside the section
- include title
- include `Original Content in English`
- include `Original Link`

For `Paper`:

- number from 1 inside the section
- include title
- include `Original Content in English`
- include `Insights in Chinese`
- include `Original Link`
- do not include a separate abstract field

Do not include summary stats, raw counts, candidate counts, build notes, delivery notes, or other internal pipeline details in the final digest.

## Paper Rules

The build script applies the fixed filter rules. Do not manually reimplement them unless the user changes the rules.

Current fixed rules:

- time window: past 24 hours by default
- paper source: `cs.AI updates on arXiv.org`
- allowed arXiv categories: `cs.LG`, `cs.CL`, `cs.SE`
- blacklist terms: `clinical`, `psychiatric`, `lung cancer`, `biomechanical`, `traffic`, `driving`, `emboli`, `field medicine`, `legal`, `graph`

Read `references/selection-notes.md` when the paper pool is ambiguous or when deciding between new-signal and core-theme papers.

## Selection Guidance

Treat these as core themes by default:

- agent
- multi-agent
- reasoning
- RAG or retrieval
- memory
- coding agents
- safety
- alignment
- efficiency

Treat papers as new signals when they introduce a new product angle, interface, modality, workflow boundary, deployment pattern, or UX implication.

Prefer papers that support a concrete insight about future AI applications. Avoid choosing routine benchmark-only papers unless the pool is thin.

## Windows UTF-8 Handling

For Chinese insights, Chinese paths, or Feishu delivery on Windows, set UTF-8 before running commands:

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
```

## Resources

- `scripts/build_digest.py`: fetches Folo data, filters papers, fetches arXiv abstracts, writes JSON and scaffold markdown
- `scripts/send_lark_markdown.py`: sends final markdown via Feishu OpenAPI using `lark-cli` credentials
- `references/selection-notes.md`: stable notes for paper bucket selection and final presentation rules
