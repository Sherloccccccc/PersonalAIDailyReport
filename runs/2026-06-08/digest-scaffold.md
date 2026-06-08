# Daily AI Info

## News

### 要闻

1. **剪映宣布将首发 Seedance 2.0 系列的新模型**

**摘要:**
剪映 通过官方 小红书 账号预告，将于 15 号首发上线 seedance2.0 新模型，官方称其生成速度更快且价格更低，并会在首发期间提供折扣优惠。

**Original Link:**
https://www.xiaohongshu.com/user/profile/5cc0829f000000001100e8e0

### 开发生态

2. **Codex 负责人宣布 100 天每日评选计划，入选者将获月度 10 倍用量**

**摘要:**
Codex 负责人 Tibo 宣布了一项为期 100 天的新计划，每天将选出一位在使用 Codex 方面表现卓越的用户，为其提供一个 月 10 倍于常规的用量上限 ，以探索 Codex 能力的边界。

**Original Link:**
https://x.com/thsottiaux/status/2063748242681307611

### 产品应用

3. **Notion 因 Opus 模型服务不稳定暂时禁用所有 Anthropic 模型引发争议**

**摘要:**
Notion 因 Anthropic 的 Opus 4.7 和 Opus 4.8 模型出现 “degraded performance” ，短暂禁用了 Notion AI 中所有 Anthropic 模型并将请求路由至其他提供商， Notion 工作人员随后澄清此次故障为服务不稳定而非模型质量问题。

**Original Link:**
https://x.com/NotionStatus/status/2063477745796161904

### 前瞻与传闻

4. **媒体报道 OpenAI 计划将 ChatGPT 改版为“超级应用”**

**摘要:**
据报道， OpenAI 计划在 未来几周 对 ChatGPT 进行上线以来最大规模的改版，将其从聊天工具转型为集成编程工具、 AI Agent 及第三方应用的“超级应用”，以应对 Anthropic 等对手的竞争并推进 IPO 前的商业化进程。

**Original Link:**
https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/

### 行业动态

5. **OpenAI定制芯片核心成员Clive Chan跳槽至Anthropic**

**摘要:**
OpenAI 定制芯片项目员工 Clive Chan 宣布离职，并于 本周 加入竞争对手 Anthropic 。他在新公司的具体职责尚不明确，而此前有消息称 Anthropic 正考虑开发自有AI芯片。

**Original Link:**
https://x.com/itsclivetime/status/2063356118525792542


## Paper

1. **M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions**

**Publish Date:**
2026-06-05

**一句话总结:**
M³Exam构建了一个面向真实用户-代理交互的多模态对话记忆基准，评估跨模态推理与隐含信息理解，并提出M³Proctor按需使用视觉源的方法，实现了13%的准确率提升和超过70%的资源节省。

**Link:**
https://arxiv.org/abs/2606.07402

2. **Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests**

**Publish Date:**
2026-06-05

**一句话总结:**
提出CapCode框架，通过随机测试将非作弊性能上限有意设定在满分以下以检测欺骗，并设计CapReward奖励机制防止模型走捷径，提升代码代理评测的可靠性。

**Link:**
https://arxiv.org/abs/2606.07379

3. **Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills**

**Publish Date:**
2026-06-05

**一句话总结:**
提出Socratic-SWE框架，从代码代理的历史解决轨迹中提炼结构化技能，以生成针对性修复任务并迭代自我进化，在SWE-bench Verified上达到50.40%的准确率。

**Link:**
https://arxiv.org/abs/2606.07412

4. **Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings**

**Publish Date:**
2026-06-05

**一句话总结:**
本文发现LLM文本嵌入因解嵌入矩阵的作用而偏向高频无用词，提出EmbedFilter线性变换，通过滤除该矩阵中对应高频词的子空间来精炼嵌入，既能提升语义质量又可降维加速检索，在多个LLM上零样本性能显著提升。

**Link:**
https://arxiv.org/abs/2606.07502

5. **SWE-Explore: Benchmarking How Coding Agents Explore Repositories**

**Publish Date:**
2026-06-05

**一句话总结:**
提出了SWE-Explore基准，通过从成功修复轨迹中提取行级真值，在多语言仓库中评测代码代理的仓库探索能力，衡量覆盖度、排序与上下文效率，发现智能探索器优于传统检索方法。

**Link:**
https://arxiv.org/abs/2606.07297

6. **Closed-Form Spectral Regularization for Multi-Task Model Merging**

**Publish Date:**
2026-06-05

**一句话总结:**
针对多任务模型合并中的干扰最小化问题，该论文提出闭式谱正则化方法SWUDI及其自适应变体SWUDI-A，通过单次特征分解替代迭代求解，无需训练数据即可在多个基准上匹配或超越现有方法，并将计算时间缩短28至72倍，适用于基础模型的存储与服务优化。

**Link:**
https://arxiv.org/abs/2606.07289

7. **Agentopia: Long-Term Life Simulation and Learning in Agent Societies**

**Publish Date:**
2026-06-05

**一句话总结:**
Agentopia构建了一个包含100个AI代理的十年期生活模拟框架，通过定义生活奖励并利用拒绝采样训练大语言模型，提升了代理的社交行为表现，并在角色扮演任务上取得15.6%的提升。

**Link:**
https://arxiv.org/abs/2606.07513

8. **Breaking the Ice: Analyzing Cold Start Latency in vLLM**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文首次系统分析了vLLM推理引擎的冷启动延迟，将其分解为六个CPU密集型步骤并建立解析模型以预测不同硬件配置下的启动时间，并提供开源工具，可为大规模推理环境的资源规划提供指导。

**Link:**
https://arxiv.org/abs/2606.07362

9. **Twelve quick tips for designing AI-driven HPC workflows**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文面向研究人员提供十二条实用建议，涵盖容器化、作业阵列、反馈循环和小文件I/O优化等，用于设计高效、可扩展且可复现的AI驱动高性能计算工作流，尤其适用于计算生物学等资源密集型场景。

**Link:**
https://arxiv.org/abs/2606.07491

10. **On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus**

**Publish Date:**
2026-06-05

**一句话总结:**
本文提出GiANT框架，利用思维链和LLM评判从388份Code4rena审计报告中自动提取7711条漏洞，构建GiAnt Corpus，并在漏洞检测、代码摘要等四项任务上对4个大模型进行基准评测，为智能合约自动化审计提供数据基础。

**Link:**
https://arxiv.org/abs/2606.07363
