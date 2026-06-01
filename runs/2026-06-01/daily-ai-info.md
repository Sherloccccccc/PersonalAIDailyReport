# Daily AI Info

## News

### 要闻

1. **MiniMax 上线 MiniMax M3 模型，支持多模态和 1M 上下文**

**摘要:**
MiniMax 上线了其新一代旗舰模型 MiniMax M3 。该模型支持原生多模态与 1M token 上下文，专为 Agent 推理及代码等场景优化，现已上线 API 和 Token Plan ，并在 OpenCode 中提供限时免费使用。更多细节有待官方的正式发布公告披露。

**Original Link:**
https://www.minimaxi.com/news/minimax-m3-zh

### 模型发布

2. **SpaceXAI 上线 Grok-Imagine-Video-1.5-Preview API**

**摘要:**
SpaceXAI 发布视频生成模型 Grok-Imagine-Video-1.5-Preview ，现已上线API。该模型支持文本和图像输入， 480p 与 720p 分辨率分别按每秒 0.08 和 0.14 美元计费。据 Arena.ai 平台数据，其 720p 版本在 Image-to-Video Arena 排行榜上位居第一。

**Original Link:**
https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview

3. **Qwen-VLA 发布，统一视觉-语言-动作建模**

**摘要:**
Qwen 团队近期发布了 Qwen-VLA 视觉-语言-动作通用模型。该模型基于 Qwen3.5-4B 构建，能统一处理机器人操作、导航和轨迹预测，官方称其在多项模拟和真实评测中表现超过专项微调模型。

**Original Link:**
https://qwen.ai/blog?id=qwenvla

### 开发生态

4. **OpenAI 宣布 Codex 用户破 500 万并重置付费用户使用额度**

**摘要:**
Codex 负责人 Tibo 宣布 Codex 用户数突破 500 万。为庆祝此里程碑，官方于 北京时间5月31日晚约11点半 面向所有 ChatGPT 付费订阅用户，重置了 Codex 的使用额度。

**Original Link:**
https://x.com/sama/status/2061097558819356732

5. **英特尔联合魔搭社区上线AI PC专区**

**摘要:**
英特尔 近期联合 魔搭 社区上线“ 英特尔 AI PC专区”，集成针对 酷睿Ultra 优化的模型库、智能体部署指南及异构计算工具，为开发者提供端侧 AI 开发实战支持。

**Original Link:**
https://modelscope.cn/brand/view/AI_PC?branch=0&amp;tree=1

6. **OpenClaw推出auto模式：LLM辅助的主机命令自动审批**

**摘要:**
OpenClaw 正公开测试名为 auto 的主机命令审批模式。该模式借助独立 LLM 审查器自动放行低风险命令，高风险或模糊情况则退回人工，兼顾了执行效率与安全。

**Original Link:**
https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals

### 行业动态

7. **SpaceXAI 招聘中文 AI Tutor 远程岗位**

**摘要:**
SpaceXAI 开放“ AI Tutor - Chinese ”远程职位，负责多语言音频标注以训练 Grok 语音交互能力，需中文母语及英语 B2 水平，时薪为 35 至 45 美元。

**Original Link:**
http://job-boards.greenhouse.io/xai/jobs/5090180007

8. **OpenAI 官宣成立 OpenAI Robotics 并启动招聘**

**摘要:**
OpenAI 首席执行官 Sam Altman 宣布其世界模拟研究项目已演变为 OpenAI Robotics 并启动招聘。该团队将招募全栈硬件、系统及 ML 工程师，旨在研发能在物理世界协助人类的机器人，短期内聚焦于支持熟练工人建设基础设施。

**Original Link:**
https://x.com/sama/status/2061117302528188712


## Paper

1. **SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks**

**Publish Date:**
2026-05-29

**一句话总结:**
提出SCOPE框架，通过挑战者与求解器双策略协同演化实现开放任务的自我对抗训练，使用自我评判生成评分细则，在多个7-8B模型上将开放任务性能最高提升10.4分，并泛化至问答任务。

**Link:**
https://arxiv.org/abs/2605.31433

2. **PithTrain: A Compact and Agent-Native MoE Training System**

**Publish Date:**
2026-05-29

**一句话总结:**
PithTrain是一个遵循代理原生设计原则的紧凑型MoE训练框架，在ATE-Bench上相比现有生产框架可减少高达62%的代理交互轮次和64%的活跃GPU时间，同时保持训练吞吐量。

**Link:**
https://arxiv.org/abs/2605.31463

3. **Evaluating Factual Density in Multi-Source RAG: A Study in Medical AI Accuracy**

**Publish Date:**
2026-05-29

**一句话总结:**
提出事实密度(FD*)检索优化方法，通过量化原子声明数与词元数的比例并消除文档长度偏差，在HealthFC医疗事实核查数据集上将系统综述证据的Top-5饱和度提升至100%，为标准RAG管道提供了低成本高精度的重排序干预。

**Link:**
https://arxiv.org/abs/2605.31506

4. **Knowledge Boundary Probing and Demand-Guided Intervention for LLM-Based Power System Code Generation**

**Publish Date:**
2026-05-29

**一句话总结:**
该论文提出PowerCodeBench基准和基于文档探查与需求引导的干预方法，显著提升开源LLM在电力系统代码生成中的准确率并降低提示成本，为无需微调的本地化AI辅助提供了可行路径。

**Link:**
https://arxiv.org/abs/2605.31478

5. **GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization**

**Publish Date:**
2026-05-29

**一句话总结:**
提出利用大语言模型作为GPU内核性能的预测器，通过选择性预测机制在不确定时回退至真实执行，结合强化学习提升预测准确率和校准度，实验表明在相同评估预算下可将候选内核数量提升数倍并找到更快内核。

**Link:**
https://arxiv.org/abs/2605.31464

6. **Preference-Aware Rubric Learning for Personalized Evaluation**

**Publish Date:**
2026-05-29

**一句话总结:**
提出PARL框架，将个性化评估建模为学习问题，从用户历史中归纳偏好感知的评分细则并通过自验证保持一致性，在真实个性化文本生成任务上显示出高保真度与跨用户泛化能力。

**Link:**
https://arxiv.org/abs/2605.31545

7. **Separating Secrets from Placeholders: A Hybrid CNN-CodeBERT Framework for Three-Class Credential Leakage Detection**

**Publish Date:**
2026-05-29

**一句话总结:**
提出CNN-CodeBERT混合框架，通过三分类（真实凭证、占位符/弱凭证、非凭证）检测代码库中的凭证泄露，在10种语言的9426样本数据集上大幅降低误报，提升占位符检测的F1分数至81%。

**Link:**
https://arxiv.org/abs/2605.31520

8. **BenHalluEval: A Multi-Task Hallucination Evaluation Framework for Large Language Models on Bengali**

**Publish Date:**
2026-05-29

**一句话总结:**
提出BenHalluEval框架，针对孟加拉语构建包含生成式问答、代码混合QA、摘要、推理四任务的12,000条幻觉样本，评估七种大模型，并设计双轨校准指标BenHalluScore以同时惩罚漏报和误报，发现链式思考提示未能稳定提升判别能力。

**Link:**
https://arxiv.org/abs/2605.31483

9. **Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning**

**Publish Date:**
2026-05-28

**一句话总结:**
PPC框架在规划之前引入预规划阶段显式理解问题类型与潜在陷阱，通过三阶段合成与复合GRPO奖励训练，在四个骨干模型和五个数学基准上提升maj@16和pass@16平均分别2.23和3.06，不增加推理开销。

**Link:**
https://arxiv.org/abs/2605.30245

10. **OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration**

**Publish Date:**
2026-05-27

**一句话总结:**
OmniVerifier-M1提出利用边界框等符号化输出作为元验证反馈，通过解耦强化学习训练视觉验证器，实现细粒度错误定位并驱动M1-TTS系统进行动态区域级自我校正。

**Link:**
https://arxiv.org/abs/2605.28805
