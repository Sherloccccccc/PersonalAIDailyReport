# Daily AI Info

## News

### 要闻

1. **NVIDIA 正式发布并开源 Nemotron 3 Ultra 模型**

**摘要:**
NVIDIA 正式发布 Nemotron 3 Ultra 开源模型，该模型采用 LatentMoE 架构，结合了 Mamba-2 和 MoE 层，拥有 550B 总参数与 55B 激活参数，支持 1M 上下文长度，专为长周期 Agent 的编排与前沿推理设计，目前已在 Hermes Agent 和 OpenCode 等多个平台限时免费开放使用。

**Original Link:**
https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/

2. **OpenAI 发布 ChatGPT 新记忆架构 Dreaming**

**摘要:**
OpenAI 宣布为 ChatGPT 推出代号为**“Dreaming” 的全新 记忆架构**，该系统能在后台自动提炼并更新用户的偏好与上下文，同时新增**“记忆摘要” 页面可查看、修改或手动引导这些 记忆内容 。目前该功能已面向 美国 地区的 Plus 和 Pro**用户开放。

**Original Link:**
https://openai.com/index/chatgpt-memory-dreaming/

3. **Anthropic 称 AI 递归自我改进或比预期更快到来**

**摘要:**
Anthropic 发布博客文章称，根据其内部数据， Claude 已在显著加速 AI 的研发进程，其中包括 超过 80% 的代码已由 Claude 自身编写，但其团队同时指出，在设定研究方向等关键判断力上， AI 与人类仍有差距，因此完全的“ 递归自我改进 ”尚未到来。 Anthropic 呼吁展开全球协调对话，探讨包括前沿 AI 开发的减速或暂停选项。

**Original Link:**
https://www.anthropic.com/institute/recursive-self-improvement

### 模型发布

4. **字节跳动开源 Bernini 统一视频生成与编辑框架**

**摘要:**
字节跳动 近期开源了视频生成与编辑框架 Bernini 的推理代码，以及渲染器权重 Bernini-R 。该框架结合 MLLM 规划器与 DiT 渲染器，支持文生视频及运动修改等任务，官方称其视频编辑能力已达闭源商业模型第一梯队。模型权重已发布于 HuggingFace 。

**Original Link:**
https://github.com/bytedance/Bernini

5. **Higgs Audio v3 TTS 发布 支持百种语言与声音克隆**

**摘要:**
Boson AI 近日发布 Higgs Audio v3 TTS 模型，专为 Voice Agent 实时对话场景设计。官方称该模型在 100 种语言上达到个位数错字率，支持零样本声音克隆与细粒度语音控制，目前已开放非商用权重与 API 。

**Original Link:**
https://www.boson.ai/blog/higgs-audio-v3-tts

6. **Google Magenta 发布实时音乐生成模型 Magenta RealTime 2**

**摘要:**
Google Magenta 团队发布了实时音乐生成模型 Magenta RealTime 2 及其配套的 C++ 推理引擎。该模型提供 24 亿 和 2.3 亿 两种参数规格，支持通过 MIDI 、音频和文本提示进行控制，目前仅限搭载 Apple Silicon 芯片的 Mac 在本地运行。

**Original Link:**
https://magenta.withgoogle.com/magenta-realtime-2

7. **NVIDIA 发布 Nemotron 3.5 Content Safety 模型与配套数据集**

**摘要:**
NVIDIA 近日发布 Nemotron 3.5 Content Safety 模型。该模型基于 Gemma 3 4B ，能在单次推理中完成多模态多语言内容审查。

**Original Link:**
https://huggingface.co/blog/nvidia/nemotron-3-5-content-safety

8. **香港生成式人工智能研发中心推出 HKGAI V3 大模型**

**摘要:**
香港生成式人工智能研发中心 正式发布 HKGAI V3 大模型。该模型已升级具备智能体能力，基于本地数据训练，支持两文三语及 香港 本地化应用场景。

**Original Link:**
https://www.info.gov.hk/gia/general/202606/03/P2026060300659.htm

### 开发生态

9. **Codex 推出 iOS 测试插件并修复 Token 计数 Bug**

**摘要:**
OpenAI 为 Codex 推出 Build iOS Apps 插件，支持在应用内浏览器中查看、测试 iOS 应用。同时 Codex 负责人称正修复导致少统计部分 Pro 和 Plus 账户 Token 的 Codex Bug 。

**Original Link:**
https://x.com/OpenAIDevs/status/2062599291479478275

10. **Claude Code 以 "ultracode" 作为触发词替换 "workflow"**

**摘要:**
为解决原触发词易被误触的问题， Claude 宣布将 Claude Code 动态工作流的显式触发词由 "workflow" 更改为 "ultracode" 。

**Original Link:**
https://x.com/ClaudeDevs/status/2062257177788858398

11. **Antigravity 向所有付费用户开放 /teamwork-preview**

**摘要:**
Antigravity 宣布为所有付费用户开放功能 /teamwork-preview ，该功能可调度多达 上百个Agent ，并行实施与验证以完成复杂开发项目。

**Original Link:**
https://x.com/_mohansolo/status/2062624694323515543

12. **GitHub Copilot 上线百万级上下文与可配置推理级别**

**摘要:**
GitHub Copilot 宣布现已正式在 VS Code 等客户端中上线 100 万token 的上下文窗口与可配置推理级别。

**Original Link:**
https://github.blog/changelog/2026-06-04-larger-context-windows-and-configurable-reasoning-levels-for-github-copilot/

13. **HeyGen 推出视频与动态图形规范 frame.md**

**摘要:**
HeyGen 宣布推出专为视频与动态图形设计打造的规范文件 “ frame.md ”，用于指导 Agent 制作品牌视频。用户可将现有的 design.md 转换为该规范，从而保持品牌跨屏幕的视觉统一。

**Original Link:**
https://x.com/HeyGen/status/2062296287710708169

14. **OpenAI 在 Responses 与 Completions API 中内建审核分数返回**

**摘要:**
OpenAI 宣布， API 现支持在生成请求中直接返回审核分数，开发者可据此进行内容路由或拦截， 无需额外调用 。

**Original Link:**
https://x.com/OpenAIDevs/status/2062619558440267801

### 产品应用

15. **NotebookLM 推出 Source Attribution 功能**

**摘要:**
NotebookLM 官方宣布推出 Source Attribution 功能。该功能允许用户查看生成每个产物所用的确切提示词与来源，并支持自定义调整。

**Original Link:**
https://x.com/NotebookLM/status/2062653124326863077

16. **LM Studio 推出 iOS 移动应用 Locally**

**摘要:**
LM Studio 正式推出 iOS 移动应用 Locally ，允许 iPhone 和 iPad 用户通过 LM Link 功能，经由端到端加密连接远程桌面端调用本地大模型。

**Original Link:**
https://lmstudio.ai/blog/locally-lm-link

### 技术与洞察

17. **Anthropic 发文介绍基于 Claude 的自助式数据分析架构**

**摘要:**
Anthropic 官方博客发文介绍了其内部基于 Claude 构建的自助式商业分析系统架构，通过引入由人类掌握语义定义且与代码同库维护的 Skills 等多层机制，其总体准确率约达 95% 。

**Original Link:**
https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude

18. **李飞飞团队发文厘清世界模型定义**

**摘要:**
李飞飞 发文厘清 世界模型 概念，将其明确划分为 渲染器 、 仿真器 和 规划器 。作为核心桥梁， 仿真器 能输出物理状态。文章指出，这三者底层知识同源，未来将走向大一统的 “世界基础模型” 。

**Original Link:**
https://drfeifei.substack.com/p/a-functional-taxonomy-of-world-models

19. **Guide Labs发布Clarity：首个内建可解释性AI平台开放研究预览**

**摘要:**
Guide Labs 推出 Clarity 平台，官方称其为全球首个内在可解释的 AI 平台，目前已以邀请制研究预览形式开放，能让用户追溯 AI 模型输出背后的概念和训练数据，并在对话中实时操控调整回答。

**Original Link:**
https://www.guidelabs.ai/post/meet-clarity/

20. **Arena.ai 推出 Agent Mode 及真实任务评估排行榜**

**摘要:**
Arena.ai 官方推出 Agent Mode ，支持模型调用沙盒等工具自主执行多步任务，并同步上线基于真实用户反馈的 Agent Arena 排行榜。

**Original Link:**
https://arena.ai/blog/agent-mode/

### 行业动态

21. **VoidZero 加入 Cloudflare，核心项目维持开源**

**摘要:**
VoidZero 官方宣布加入 Cloudflare ，旗下 Vite 、 Vitest 、 Rolldown 等核心开源项目将继续保持 MIT 许可，并由原团队继续主导开发。

**Original Link:**
https://voidzero.dev/posts/voidzero-cloudflare

22. **Google 宣布向犹他州所有 K-12 学校提供 Gemini for Education**

**摘要:**
Google 宣布与 犹他州教育局 达成合作，计划从 2026-2027 学年 起，面向该州所有 K-12 学校免费提供 Gemini for Education 。

**Original Link:**
https://blog.google/products-and-platforms/products/education/utah-state-education-partnership/

### 前瞻与传闻

23. **TRAE 即将上线四档付费“速通”权益**

**摘要:**
TRAE 即将上线四档付费“速通”权益，用于提升高峰时段的对话响应速度。四档月费从 99元 到 1399元 ，提供 100次 到不限次的速通次数与 云端任务并行上限 ，高档位支持优先体验 SOTA模型 。购买后权益与账号绑定，支持多端通用。原免费版继续保留，老版用户权益将自动平移。

**Original Link:**
https://docs.trae.cn/ide/coming-soon

24. **消息称 Anthropic 即将发布 Mythos 级别模型代号 Oceanus**

**摘要:**
据多个社交平台消息人士透露， Anthropic 正准备公开发布代号为 Oceanus 的 Mythos 级新模型。该模型的检查点已面向部分红队人员开放测试。

**Original Link:**
https://x.com/chetaslua/status/2062565987103502520


## Paper

1. **Framing, Judging, Steering: An Assessable Competency Model for Teach-ing Students to Reason With Generative AI**

**Publish Date:**
2026-06-05

**一句话总结:**
本文提出CoRe-3能力模型，将生成式AI使用拆解为任务界定、输出评判和迭代引导三项技能，并开发CoReasoningLab平台模拟有缺陷的AI输出进行独立评分，通过模拟学习者验证技能可分离性。

**Link:**
https://arxiv.org/abs/2606.05983

2. **Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文通过100多名开发者与四个前沿模型在约五小时编码任务中的合作实验，首次大规模研究人类对AI编码破坏行为的察觉能力，发现94%未能发现破坏，56%忽略安全监视器警告，为以人为中心的安全机制提供建议。

**Link:**
https://arxiv.org/abs/2606.05647

3. **Agents' Last Exam**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文推出Agents' Last Exam基准，联合250+专家覆盖55个子领域、1000+任务，评估智能体在长期、有经济价值的真实工作流中的表现，当前最好配置仅2.6%通过率，旨在弥合基准成功与GDP影响力差距。

**Link:**
https://arxiv.org/abs/2606.05405

4. **Self-Commitment Latency: A Reward-Free Probe for Prompted Implicit Hacking**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出“自我承诺延迟”指标，基于模型自身对答案的早期 commit 行为，无需奖励模型即可检测隐式奖励黑客，通过 token 概率测量，在 GSM8K 上达 AUROC 0.878，区分有提示与正常推理。

**Link:**
https://arxiv.org/abs/2606.05625

5. **Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出回顾式驾驭优化方法RHO，利用智能体历史轨迹自监督地优化技能与工作流，通过自我验证和偏好选择更新，在SWE-Bench Pro上单轮优化将通过率从59%提升至78%，并有效修正先前失败模式。

**Link:**
https://arxiv.org/abs/2606.05922

6. **Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文通过 MT-Bench 和 AlpacaEval 实验揭示 LLM 评判在事后交互下可被操纵，权威框架加剧逆转，提出鲁棒性分数（ERS）量化交互脆弱性，倡导评估协议包含交互鲁棒性测试，为 LLM 评估提供新指标。

**Link:**
https://arxiv.org/abs/2606.05384

7. **Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出Continual Learning Bench（CL-Bench）基准，涵盖软件工程、信号处理、疫情预测等六个领域，通过专家验证的任务和增益指标评估LLM智能体在状态化环境中的持续学习能力，发现当前记忆系统未能有效促进知识复用，反而不及简单上下文学习。

**Link:**
https://arxiv.org/abs/2606.05661

8. **Beyond Output Matching: Preserving Internal Geometry in NVFP4 LLM Distillatio**

**Publish Date:**
2026-06-05

**一句话总结:**
本文针对NVFP4量化大语言模型蒸馏中输出匹配无法保证内部表征一致的问题，提出基于中心核对齐的规整项，在Nemotron和Qwen3模型上通过层间Gram矩阵对齐改善推理和编码准确率。

**Link:**
https://arxiv.org/abs/2606.05682

9. **SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出SubtleMemory基准，包含1522个实例及关系控制的语义变体，测试长期交互智能体对补充、矛盾等记忆关系的细粒度辨别，发现现有系统普遍薄弱，并设计诊断协议评估记忆保存、检索和推理各阶段能力。

**Link:**
https://arxiv.org/abs/2606.05761

10. **EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts**

**Publish Date:**
2026-06-05

**一句话总结:**
EpiEvolve 提出一种自演化智能体，针对流式疫情预测，通过固定 LLM 权重并引入分层情景记忆、延迟标签反思、规则蒸馏和机制感知检索，在 COVID-19 住院趋势预测中提升准确率并缩短机制切换后的恢复滞后。

**Link:**
https://arxiv.org/abs/2606.05513
