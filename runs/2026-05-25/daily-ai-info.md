# Daily AI Info

## News

### 要闻

1. **DeepSeek 昨日下午突发故障并迅速恢复**

**摘要:**
DeepSeek 的状态页显示，其 API 与网页对话服务在 5 月 24 日 下午突发不可用故障，经紧急排查与修复，现已完全恢复正常，官方记录此次故障总时长约为 18 分钟 。

**Original Link:**
https://status.deepseek.com/incidents/6480608319287

### 行业动态

2. **vLLM 封禁为刷简历提交无意义 PR 的贡献者**

**摘要:**
vLLM 官方封禁了一名为了丰富简历而提交无意义 PR 的贡献者。同时 vLLM 称，解决真实生产问题的开发者，只要使用可验证的公司或大学邮箱向指定邮箱发送申请，就能获得代码的优先审查。

**Original Link:**
https://x.com/vllm_project/status/2058358072020779391

### 前瞻与传闻

3. **Codex 负责人探讨为产品引入 /slow mode 批量计算功能**

**摘要:**
Codex 负责人 Tibo 发起提问，探讨是否为 Codex 引入 /slow mode 批量计算功能 。该提议目前仅处于初步讨论，尚未确认落地。

**Original Link:**
https://x.com/thsottiaux/status/2058320061258236263

4. **claude-opus-4.8 疑似现身 Google Vertex 后台**

**摘要:**
有用户称， Google Vertex 上曾出现了 claude-opus-4.8 。同时，另有用户称 Anthropic 预计在 6 月中下旬 发布 Sonnet 4.8 。上述信息均为非官方信息。

**Original Link:**
https://x.com/marmaduke091/status/2058324267817750820


## Paper

1. **OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents**

**Publish Date:**
2026-05-22

**一句话总结:**
OpenSkillEval是一个自动评估框架，通过动态生成演示文稿生成、网页设计等五类下游应用的任务实例，系统评估了30多个开源技能和多个模型/代理框架，发现技能增强的效果依赖于底层模型和框架，且许多流行技能并不优于基础代理，为技能的设计与选择提供了实用指导。

**Link:**
https://arxiv.org/abs/2605.23657

2. **HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored Search Retrieval**

**Publish Date:**
2026-05-22

**一句话总结:**
本文提出HARNESS-LM三阶段训练方案（教师微调、L2对齐蒸馏与对比精炼），将十亿参数SLM的知识迁移至1.9亿参数模型，在Bing Ads评估中恢复98%以上精度，且在线延迟降低27倍、吞吐提升20倍，A/B测试实现收入提升1%。

**Link:**
https://arxiv.org/abs/2605.23572

3. **Cost-Effective Model Evaluation with Meta-Learning**

**Publish Date:**
2026-05-22

**一句话总结:**
提出MetaEvaluator，利用参考模型池上的元学习获得可迁移初始化，实现在无标注数据上对未见模型进行跨架构、跨模态的低成本性能预估，大幅降低评估开销，实验表明其能稳定生成准确的性能估计，使新兴模型的可扩展基准测试成为可能。

**Link:**
https://arxiv.org/abs/2605.23595

4. **SkillOpt: Executive Strategy for Self-Evolving Agent Skills**

**Publish Date:**
2026-05-22

**一句话总结:**
SkillOpt 训练一个独立的优化器模型对 Agent 技能文档进行可控制的增删改编辑，仅当验证集严格提升才接受，在三个执行环境中全面超越人工、大模型一次生成和各类自改进基线，并验证跨模型、跨环境的技能迁移。

**Link:**
https://arxiv.org/abs/2605.23904

5. **Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems**

**Publish Date:**
2026-05-22

**一句话总结:**
作者在BEIR和意大利语RAG任务上对比了Google Embeddings 2与五个开源嵌入模型，发现GE2精度最高但延迟是本地模型的14倍，而多语言E5模型在延迟敏感场景下更具优势，并分析了不同分块策略的影响。

**Link:**
https://arxiv.org/abs/2605.23618

6. **Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents**

**Publish Date:**
2026-05-22

**一句话总结:**
本文提出定量目标持久性概念及PushBench基准，通过状态跟踪与积压控制器让agent在工件收集任务中坚持至计数完成，Claude Code与Codex CLI在100工件任务上仅获3/9成功，揭示长程agent需维护验证进度方可可靠完成定量目标。

**Link:**
https://arxiv.org/abs/2605.23574

7. **CVSearch: Empowering Multimodal LLMs with Cognitive Visual Search for High-Resolution Image Perception**

**Publish Date:**
2026-05-22

**一句话总结:**
CVSearch 提出一种无需训练的自适应框架，先尝试专家辅助搜索，失败时触发语义感知的 bottom-up 扫描，在多个高分辨率基准上达到最优精度并显著提升搜索效率，代码已开源。

**Link:**
https://arxiv.org/abs/2605.23655

8. **Decomposing Queries into Tool Calls for Long-Video Keyframe Retrieval**

**Publish Date:**
2026-05-22

**一句话总结:**
本文提出ToolMerge方法，通过LLM将查询分解为多种工具调用并按布尔操作符合并排名，在新建的Molmo-2 Moments基准上进行长视频关键帧检索，字幕检索性能优于现有方法5%，并开源代码与数据。

**Link:**
https://arxiv.org/abs/2605.23826

9. **Agentic Proving for Program Verification**

**Publish Date:**
2026-05-22

**一句话总结:**
评估 Claude Code 在 CLEVER Lean 4 基准上进行代理式的程序验证，98.8% 的问题生成有效规范，端到端成功率 98.1%，并指出原有基准难度不足、需要更严格评估方法。

**Link:**
https://arxiv.org/abs/2605.23772

10. **How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness**

**Publish Date:**
2026-05-22

**一句话总结:**
将基准测试中的数据集视为投票者、模型视为候选人，从社会选择理论角度分析通过训练特定数据集操纵排行榜的难度，证明在Borda计数和平均胜率下为NP难问题，并引入实例级鲁棒性指标，在MMLU和BIG-Bench Hard上评估了不同聚合方法抵御操纵的能力。

**Link:**
https://arxiv.org/abs/2605.23628
