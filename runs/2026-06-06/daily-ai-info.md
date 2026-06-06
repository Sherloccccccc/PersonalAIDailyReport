# Daily AI Info

## News

### 要闻

1. **OpenAI 确认系统 Bug 导致部分账户被误封**

**摘要:**
OpenAI 官方确认，系统 Bug 导致部分用户账户被错误暂停，目前已恢复访问，但仍在处理受影响用户的订阅和额度异常，并将发送邮件通知。

**Original Link:**
https://x.com/OpenAI/status/2062927046448431587

2. **OpenAI 发布 Codex 更新：新增设置搜索与状态保存功能**

**摘要:**
OpenAI 为 Codex 应用发布了多项更新。新版新增带分类结果的设置搜索，支持全屏下侧边聊天可见，重启后也会自动恢复提示词草稿以及 工作树 上下文等工作状态。

**Original Link:**
https://x.com/OpenAIDevs/status/2062987643286438337

3. **ChatGPT web端writing blocks新增直接发送邮件功能**

**摘要:**
ChatGPT 宣布一项web端新功能：现在可以在对话界面的 writing blocks 中直接起草邮件、进行修改，并一键发送，所有操作无需离开当前聊天会话。

**Original Link:**
https://x.com/ChatGPTapp/status/2062944254591430917

### 模型发布

4. **Google 发布 Gemma 4 QAT 权重及全新移动端量化格式**

**摘要:**
Google DeepMind 发布 Gemma 4 量化感知训练checkpoints。同时官方引入全新移动端量化格式，利用定向 2-bit 压缩等技术，将 Gemma 4 E2B 模型内存占用降至约 1GB 。相关模型权重已上线 Hugging Face ，支持多种工具链部署。

**Original Link:**
https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/

5. **小红书 rednote-hilab 开源 20 亿参数 dots.tts**

**摘要:**
小红书 rednote-hilab 开源了 20 亿参数的端到端文本转语音模型 dots.tts 。官方称其在多项基准测试中达开源 SOTA 。该模型的多版本权重与推理代码已基于 Apache 2.0 协议发布。

**Original Link:**
https://rednote-hilab.github.io/dots.tts-demo/

6. **OpenRouter上线图像模型Riverflow 2.5并提供限时免费调用**

**摘要:**
OpenRouter 上线首个可自定义评分标准的图像模型 Riverflow 2.5 。用户可控制评分准则引导思维与编辑。该模型在 6 月 9 日 前免费开放使用。

**Original Link:**
https://x.com/OpenRouter/status/2062951474406240687

### 开发生态

7. **Vercel 上线 skills.sh API 支持查询超 60 万开源技能**

**摘要:**
Vercel 宣布 skills.sh API 现已上线。开发者使用 Vercel OIDC token 认证，即可查询开源生态中超 60 万 个 skills 的详情与安全审计。

**Original Link:**
https://vercel.com/changelog/the-skills-sh-api-is-now-available

8. **Cursor 更新 Design Mode 支持可视化修改 UI**

**摘要:**
Cursor 更新 Design Mode ，允许开发者在内置浏览器中通过点击、绘制或语音提示修改 UI，并交由 Agent 直接编辑底层源代码。

**Original Link:**
https://cursor.com/blog/browser-visual-editor

9. **阿里巴巴推出 Open Code Review 混合架构代码审查工具**

**摘要:**
阿里巴巴 近期在 GitHub 开源了其内部 AI 代码审查工具 Open Code Review ，采用确定性工程管线与 LLM Agent 混合架构，兼容 OpenAI 与 Anthropic API 。

**Original Link:**
https://alibaba.github.io/open-code-review/

10. **Google 推出开源工具 Google Colab CLI**

**摘要:**
Google 宣布推出轻量级开源工具 Google Colab CLI ，打通本地终端与远程 Colab 运行时，支持开发者及 AI Agent 直接调用 GPU / TPU 算力执行 ML 流水线。

**Original Link:**
https://developers.googleblog.com/introducing-the-google-colab-cli/

11. **Google 推出面向企业的 Agentic RAG 框架**

**摘要:**
Google Research 与 Google Cloud 联合推出全新的 Agentic RAG 框架，该系统采用多智能体架构，通过核心的 Sufficient Context Agent 评估上下文完整性并触发迭代检索，官方称其比标准 RAG 准确率最高提升 34% 。

**Original Link:**
https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/

### 产品应用

12. **Claude 限时提供 Claude Cowork 翻倍使用量限额，面向所有付费用户**

**摘要:**
Claude 官方宣布已将 Claude Cowork 的使用限额翻倍，即日起面向所有付费计划生效，持续至 7 月 5 日 。

**Original Link:**
http://claude.com/cowork

13. **Kimi Work 桌面端 Windows 版已可用**

**摘要:**
Kimi Work 的 Windows 版已正式上线。该产品内置 300 个 Agent ，可全天候自动化执行任务。

**Original Link:**
https://www.kimi.com/zh-cn/products/kimi-work

14. **抖音副总裁回应豆包误判蘑菇传闻**

**摘要:**
抖音 副总裁 李亮 回应“ 豆包 误判蘑菇致中毒”传闻称， 豆包 识别时已提示 剧毒混淆风险 并建议 勿食 ，强调 AI 仅供参考 ，涉及 安全 务必多方求证。

**Original Link:**
https://weibo.com/7965906915/R2HT50wwm

### 技术与洞察

15. **腾讯混元与人大团队开源 PlanningBench 规划基准**

**摘要:**
腾讯混元 与 人大 团队开源 PlanningBench 基准，用于大模型复杂规划任务的评估与训练，现已发布 467 个合成评估实例。

**Original Link:**
https://github.com/Tencent-Hunyuan/PlanningBench

16. **通义实验室开源通用智能体评测基准 PawBench**

**摘要:**
通义实验室 推出并开源评测基准 PawBench 。该基准面向通用智能体，通过 150 道任务评测底座模型与运行框架的联合效果，帮助开发者精准定位问题。

**Original Link:**
https://agentscope-ai.github.io/PawBench

17. **Anthropic 发表白皮书：Claude Opus 4.7 在 NMR 光谱预测中比肩专业软件**

**摘要:**
Anthropic 发表白皮书称，未做化学专属微调的 Claude Opus 4.7 ，在 NMR 氢谱前向预测中平均误差与专业软件 ChemDraw 和 MestReNova 相当或更优，还可从一维谱图反推分子结构。

**Original Link:**
https://www.anthropic.com/research/making-claude-a-chemist

### 行业动态

18. **Google将向SpaceX支付每月9.2亿美元用于算力租赁**

**摘要:**
据监管文件披露， SpaceX 与 Google 签署新的云计算服务协议， Google 将支付每月 9.2 亿美元 ，以获取位于 Memphis 数据中心约 11 万 个 NVIDIA GPU 的算力资源。

**Original Link:**
https://www.sec.gov/Archives/edgar/data/1181412/000162828026041150/spacexagreementfwp.htm

19. **多家巨头 AI 预算超支，行业转向成本管控**

**摘要:**
据报道，随着 AI 智能体导致 Token 消耗剧增，多家科技企业因预算失控开始限制内部 AI 支出。 Linux Foundation 宣布成立 Tokenomics Foundation 旨在制定计费标准。

**Original Link:**
https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs

20. **基于阿里千问微调，NBA官方大模型“NBA Chat”上线**

**摘要:**
NBA中国与 阿里 联合打造的首个官方大模型 NBA Chat 正式上线，球迷现可在官方APP内体验基于 千问 大模型的智能篮球问答服务。

**Original Link:**
https://mp.weixin.qq.com/s/BAfhxzLLa1m6xQ-cBCaxxw

### 前瞻与传闻

21. **报道称 Meta 拟在路易斯安那州建 2000 亿美元数据中心并考虑发售新股融资**

**摘要:**
媒体报道称 Meta 将在 路易斯安那州 建设投资额达 2000 亿美元 的数据中心。另有消息称，为维持 AI 支出，该公司正考虑发售数百亿美元新股。

**Original Link:**
https://www.bloomberg.com/news/videos/2026-06-05/the-200-billion-data-center-transforming-louisiana-video


## Paper

1. **You Only Index Once: Cross-Layer Sparse Attention with Shared Routing**

**Publish Date:**
2026-06-04

**一句话总结:**
该论文提出跨层稀疏注意力（CLSA），在YOCO等KV共享架构中，单个索引器一次计算token级top-k选择并跨解码层共享，在128K上下文下实现7.6倍解码加速和17.1倍吞吐提升，兼顾准确性与效率，为长上下文LLM提供完整架构方案。

**Link:**
https://arxiv.org/abs/2606.06467

2. **More than a Judge: An Empirical Study of Agent-Human Interaction in Crowdsourced Testing Assessment**

**Publish Date:**
2026-06-04

**一句话总结:**
通过20名测试者在三个真实应用上的四阶段受控实验，发现多智能体评估系统生成的反馈不仅改善即时报告修订，还提升新任务首次提交质量和跨应用实践迁移，结合事后问卷证实反馈被理解、采纳并延续，表明评估智能体可成为上游报告质量改进的工作流集成反馈提供者。

**Link:**
https://arxiv.org/abs/2606.06301

3. **Self-Augmenting Retrieval for Diffusion Language Models**

**Publish Date:**
2026-06-04

**一句话总结:**
SARDI框架利用扩散语言模型去噪过程中丢弃的低置信度令牌作为前瞻信号，在生成过程中动态触发检索以获取更强证据，无需训练且与检索器无关，在五个多跳问答基准上以最高8倍吞吐量超越现有训练无关的扩散和自回归检索基线。

**Link:**
https://arxiv.org/abs/2606.06474

4. **Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Code-Generation Skill**

**Publish Date:**
2026-06-04

**一句话总结:**
通过预注册的双模型消融实验，对比完整波普尔式技能、纯标签框架、长度匹配安慰剂与执行神谕，发现大型模型因天花板效应未显示增益，小型模型的结构化提示提升20-22个点的执行正确率但程序内容无额外收益，表明收益归因于框架结构，提供校准性负面结果及可复用的提示技能评估协议。

**Link:**
https://arxiv.org/abs/2606.06454

5. **PAMF: Prior-Aware Multimodal Fusion for Incomplete Time Series Data**

**Publish Date:**
2026-06-04

**一句话总结:**
该论文提出PAMF框架，针对多模态时间序列中的单一模态内缺失和整个模态缺失，使用先验感知的流匹配与权重共享编码器连接填补与分类，在多个医疗时间序列基准上取得最优下游性能，为不完整数据的融合提供了新方案。

**Link:**
https://arxiv.org/abs/2606.06328

6. **Unsupervised Skill Discovery for Agentic Data Analysis**

**Publish Date:**
2026-06-04

**一句话总结:**
DataCOPE提出无监督技能发现框架，通过自适应检查表验证器与答案一致性验证器从探索轨迹中提取信号，迭代蒸馏可复用数据分析技能，在报告和分析任务上平均提升9.71%和32.30%。

**Link:**
https://arxiv.org/abs/2606.06416

7. **SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出SoCRATES评测基准，覆盖八个领域和五种社会认知变化轴，通过真实冲突场景和话题定位评估器测试LLM调解能力，发现当前最佳模型仅能缩小约三分之一的分歧，且对社会认知条件适应不足。

**Link:**
https://arxiv.org/abs/2606.05563

8. **Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文提出将统计偏好学习与语义意图解析解耦的局部驾驭架构，通过本地统计结果影响远程大模型技能选择，在评测中实现最低累积遗憾和最高准确率，效果优于传统记忆增强智能体。

**Link:**
https://arxiv.org/abs/2606.05828

9. **EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading**

**Publish Date:**
2026-06-04

**一句话总结:**
EDIT通过诊断模型内部信念和证据基础信号定位评分推理错误，分阶段进行局部修正和信念引导的强化学习校准，在多学科评分基准上显著提升了评分规则忠实性，该方法结合监督微调与强化学习，解决自动评分中的可解释性难题。

**Link:**
https://arxiv.org/abs/2606.06350

10. **Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning**

**Publish Date:**
2026-06-03

**一句话总结:**
论文提出CHERRL，一个用于研究基于量规的强化学习中奖励欺骗的可控环境，通过向LLM裁判注入已知偏见来稳定复现欺骗行为，并从可发现性与可剥削性两个角度分析偏见影响，同时开发基于代理的系统从训练日志自动检测欺骗发生点，代码已公开。

**Link:**
https://arxiv.org/abs/2606.04923
