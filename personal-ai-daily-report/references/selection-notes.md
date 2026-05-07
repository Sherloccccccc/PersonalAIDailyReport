# Selection Notes

Use these notes for the `Paper` module of `Daily AI Info`.

## Source Order

1. arXiv API
2. arXiv RSS fallback

The fallback path exists because arXiv API may hang, fail, or hit rate limits. Build logs must preserve which source was used.

## Hard Filter

Keep papers only when they pass both checks:

- categories intersect with `cs.LG`, `cs.CL`, `cs.SE`
- title/abstract do not contain blacklist terms

Blacklist:

- `clinical`
- `psychiatric`
- `lung cancer`
- `biomechanical`
- `traffic`
- `driving`
- `emboli`
- `field medicine`
- `legal`
- `graph`

## Score Dimensions

Total score is 100 points:

| Dimension | Points | Meaning |
|---|---:|---|
| `application_relevance` | 25 | Can inform AI products, agents, workflows, tools, or developer experience |
| `new_signal` | 25 | New task, interface, dataset, benchmark, deployment pattern, or usage mode |
| `engineering_utility` | 25 | Can plausibly be implemented, integrated, tested, or reused |
| `timeliness_rarity` | 25 | Fits current AI trends or is rare enough to be worth attention |

Current threshold: `score_total >= 60`.

## State Rules

`data/paper-state.json` is a single table.

- `if_pushed = 0`: waiting list
- `if_pushed = 1`: already sent

Do not migrate rows between separate waiting/sent lists. Select from `if_pushed = 0` by `score_total` descending.

Store full abstract in the state file for later audit.

## Summary Rules

Paper `一句话总结` should be around 80-120 Chinese characters, must be Chinese, and answer:

- What did the paper build/propose/evaluate?
- What concrete task, benchmark, dataset, method, system, or result is involved?
- Why does it matter for AI products, agents, tools, or workflows?

Good:

```text
提出 MOSAIC-Bench，把 coding agent 的安全评测从单次提示扩展到多阶段工程任务，检查连续无害改动是否会组合成可利用漏洞，覆盖199 three-stage attack chains、10 web-application substrates、31 CWE classes；实验还比较 staged tickets 与 direct prompt，并评估 reviewer 是否会把漏洞 PR 当作常规改动放行。
```

Bad:

```text
这篇论文围绕某主题展开，提供了工程线索。
```

Forbidden generic phrases:

- `围绕...展开`
- `核心贡献是：We introduce...`
- raw English contribution sentences copied from abstracts
- `工程线索`
- `新方法、评测或工程线索`

## Final Presentation Rules

Do not show score, abstract, candidate counts, source fallback details, or logs in the daily report body.

Show only:

- paper title
- publish date
- 一句话总结
- link
