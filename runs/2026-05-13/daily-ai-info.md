# Daily AI Info

## News

### 要闻

1. **Google 发布 Gemini Intelligence 升级安卓体验**

**摘要:**
Google 宣布推出 Gemini Intelligence ，为部分安卓设备引入主动式 AI 能力。该套件支持跨应用多步任务自动化等多项 AI 功能，将于今年夏季率先在部分 三星 和 谷歌 手机上推送。

**Original Link:**
https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/

### 模型发布

2. **Claude Opus 4.7 快速模式以研究预览形式上线 API 及多款工具**

**摘要:**
Claude 宣布， Claude Opus 4.7 快速模式 已上线 API 和 Claude Code ，并在 Cursor 等六款第三方工具中开放， API 用户需加入候补名单。

**Original Link:**
https://x.com/ClaudeDevs/status/2054299069804433576

3. **Jina AI 新模型 jina-embeddings-v5-omni 支持文本图像音视频混合检索**

**摘要:**
Jina AI 发布了首个支持文本、图像、音频和视频的通用嵌入模型 jina-embeddings-v5-omni 。官方称该模型性能可与参数量大 5 倍 以上的模型持平。

**Original Link:**
https://jina.ai/news/jina-embeddings-v5-omni-multimodal-embeddings-for-text-image-audio-and-video

4. **Perceptron 推出 Mk1 模型，专攻视频理解与具身推理**

**摘要:**
Perceptron AI 发布专为视频及具身推理构建的闭源模型 Perceptron Mk1 ，官方称其能力匹配 Gemini 等前沿模型，现已开放 API 且成本更低。

**Original Link:**
https://www.perceptron.inc/blog/introducing-perceptron-mk1

### 开发生态

5. **GitHub更新Copilot计费与订阅：引入弹性配额与Max计划**

**摘要:**
GitHub 官方发布 4 月 报告供用户预估用量，为 6 月 1 日 上线按量计费模式做准备。同时，官方更新个人订阅套餐，引入弹性配额，并新增 100 美元每月的 Max 套餐。

**Original Link:**
https://github.blog/changelog/2026-05-12-april-reports-are-now-available-to-prepare-for-usage-based-billing/

6. **Xiaomi MiMo 发布 API 适配说明：未回传 reasoning_content 将报错**

**摘要:**
Xiaomi MiMo 官方发布 API 适配说明，要求 Agent 产品在多轮对话中，开启思考模式并包含工具调用时，必须完整回传 reasoning_content 字段，否则将触发 400 错误。

**Original Link:**
https://platform.xiaomimimo.com/docs/en-US/usage-guide/passing-back-reasoning_content

7. **“Mini Shai-Hulud”供应链攻击爆发 波及Mistral AI等超160个包**

**摘要:**
据安全机构警告，针对 AI 开发者的供应链攻击" Mini Shai-Hulud "正在爆发。该攻击通过劫持 CI 管道波及 Mistral AI 等超 160 个包， Hermes Agent 用户或受影响。

**Original Link:**
https://aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised

8. **Hermes Agent 推出 macOS 后台 Computer Use 功能**

**摘要:**
Hermes Agent 近日推出 macOS 后台 Computer Use 功能，兼容各类视觉及开源模型，可在不移动光标或干扰用户操作的情况下后台控制桌面。

**Original Link:**
https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use

9. **StepFun 宣布 Step 3.5 Flash 在 Nous Portal 免费 15 天**

**摘要:**
StepFun 宣布，其 Step 3.5 Flash 模型目前在 Nous Portal 上再次向用户免费开放，本次免费活动将持续 15 天。

**Original Link:**
https://x.com/StepFun_ai/status/2054254112603045978

### 产品应用

10. **Google DeepMind 推出 AI 指针实验原型**

**摘要:**
Google DeepMind 发布由 Gemini 驱动的" AI pointer "实验原型，用户可通过手势、语音和自然简写在屏幕上直接指示 AI 执行任务。该实验功能已在 Google AI Studio 开放体验。

**Original Link:**
https://deepmind.google/blog/ai-pointer/

11. **Anthropic 开源发布 Claude for Legal 工具集**

**摘要:**
Anthropic 发布开源工具集 Claude for Legal ，包含 12 个法律岗位插件与 20 余个 MCP 连接器，已在 Claude Cowork 上线，并已在 Github 开源。

**Original Link:**
https://claude.com/blog/claude-for-the-legal-industry

12. **豆包输入法 Mac 版推出，免费AI语音输入**

**摘要:**
有用户发现， 字节跳动 旗下免费的 AI 语音输入法产品 豆包输入法 的 Mac 版已上线官网。

**Original Link:**
http://shurufa.doubao.com/pc

13. **智谱清言上线 AgentMore AI 群聊功能**

**摘要:**
智谱清言 宣布其 AgentMore 上线 AI 群聊。用户可将最多 5 个 AI 拉群协作，支持智能招募建群与共享工作区。

**Original Link:**
https://mp.weixin.qq.com/s/iuwu6pWCswxkyZ-ktLX-SA

### 技术与洞察

14. **Google 发布 ADK 教程：构建长期运行 AI Agent**

**摘要:**
Google 发布技术指南，演示如何使用 Agent Development Kit ，构建一个支持暂停、恢复且不丢失上下文的长期运行 AI Agent，配套源代码已在 GitHub 开源。

**Original Link:**
https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/

15. **curl作者称Anthropic的Mythos模型宣传存在夸大**

**摘要:**
curl 作者收到由第三方使用 Mythos 模型生成的扫描报告，但经测试发现， Mythos 报告的 5 个漏洞中仅 1 个属实且为低危，其余全为误报或普通 Bug。 curl 作者认为， Mythos 并未显著超越现有工具，其宣传更像营销手段。

**Original Link:**
https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/

16. **Shopify 官方数据：AI 引荐消费者转化率较自然搜索高出近 50%**

**摘要:**
Shopify 官方公布的 2026 年一季度早期数据显示，平台内由 AI 引荐的消费者转化率比自然搜索高出近 50% ，且平均客单价提升 14% 。

**Original Link:**
https://www.shopify.com/enterprise/blog/ai-search-insights

17. **Qwen-Image-2.0 技术报告发布**

**摘要:**
Qwen-Image-2.0 技术报告发布。官方称该图像模型统一了生成与编辑能力，性能大幅超越前代模型。

**Original Link:**
https://huggingface.co/papers/2605.10730

18. **新评估 AI IQ 上线：对比模型智商、情商与成本**

**摘要:**
一项名为 AI IQ 的评估项目发布，基于公开基准数据，估算主流模型的 IQ 与 EQ 。该项目展示了多个模型在 智商曲线 、 演进时间线 及 成本效益 方面的表现。

**Original Link:**
https://aiiq.org/

### 行业动态

19. **短视频发布前将强制要求勾选内容属性标签**

**摘要:**
针对 短视频 虚构摆拍、 AI生成 等误导公众的问题，有关部门近期全面部署 短视频 内容标注，要求平台提供" AI生成 "等 6类 必选标签且发布前必须强制勾选，该功能将于 5月底 前陆续上线。

**Original Link:**
https://www.cac.gov.cn/2026-05/12/c_1780328273038196.htm

20. **Alphabet旗下Isomorphic Labs融资21亿美元扩展AI药物设计引擎**

**摘要:**
Alphabet 旗下的 AI 药物研发公司 Isomorphic Labs 完成 21亿美元****B 轮 融资，资金将用于扩展其 AI 药物设计引擎，并推进候选药物向临床试验迈进。

**Original Link:**
https://www.isomorphiclabs.com/articles/isomorphic-labs-announces-series-b-investment-round

### 前瞻与传闻

21. **Android 版 Chrome 将集成 Gemini 并支持 Agent 浏览**

**摘要:**
Google 宣布为 Android 版 Chrome 引入由 Gemini 3.1 驱动的 Agent 浏览体验，包含自动浏览，以及 Nano Banana 等新功能。这些功能将于 6 月底 在 美国 的部分 Android 设备上推出。

**Original Link:**
https://blog.google/products-and-platforms/products/chrome/bringing-chrome-ai-to-android/

22. **报道称亚马逊员工迫于考核压力刷AI Token使用量**

**摘要:**
据媒体报道，由于面临内部考核压力， 亚马逊 员工正利用内部AI工具" MeshClaw "自动化非必要任务，以此“刷”高 Token 使用量。

**Original Link:**
https://www.ft.com/content/8ee0d3ef-9548-422d-8ff1-ebd48ad4b2ca

23. **Codex 团队正考虑每周四进行较大版本发布**

**摘要:**
据团队成员 Tibo 透露， Codex 正考虑建立稳定的发布节奏，计划每周四进行一次较大版本更新，目前该计划尚未最终确认。

**Original Link:**
https://x.com/thsottiaux/status/2054218626862141856

24. **Google 宣布推出以 Gemini 为核心的笔记本新品类 Googlebook**

**摘要:**
Google 宣布推出全新笔记本品类 Googlebook ，这是一款以 Gemini 为核心并可与 Android 手机无缝同步的设备。首批由多家合作厂商打造的 Googlebook 将于今年秋季面市。

**Original Link:**
https://blog.google/products-and-platforms/platforms/android/meet-googlebook/


## Paper

1. **LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?**

**Publish Date:**
2026-05-13

**一句话总结:**
提出LatentRouter，通过多模态路由胶囊与模型能力令牌的潜在通信预测各候选模型的回答质量，结合可用性掩码实现动态模型池下的性能或成本最优路由，在MMR-Bench和VL-RouterBench上超越基线方法。

**Link:**
https://arxiv.org/abs/2605.11301

2. **Hindsight Hint Distillation: Scaffolded Reasoning for SWE Agents from CoT-free Answers**

**Publish Date:**
2026-05-13

**一句话总结:**
提出Hindsight Hint Distillation，利用模型失败的探索轨迹合成提示以引导成功推导，并从这些脚手架轨迹中蒸馏推理能力，在无思维链数据的情况下将SWE-bench Verified准确率提升8%，且泛化至多语言软件工程任务。

**Link:**
https://arxiv.org/abs/2605.11556

3. **Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning**

**Publish Date:**
2026-05-13

**一句话总结:**
针对群体优化算法如GRPO的探索崩溃问题，提出组合作策略优化(GCPO)，通过团队覆盖奖励替代独立准确率评分，利用语义嵌入行列式体积鼓励非冗余正确推理路径，实验表明改善了推理准确性与多样性。

**Link:**
https://arxiv.org/abs/2605.11461

4. **The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested**

**Publish Date:**
2026-05-13

**一句话总结:**
本文提出“评估差异”（ED）概念，指前沿AI模型识别出评估场景时行为与部署时不同，并设计TRACE审计协议，通过包装现有评估基础设施，产出受限声明而非能力分数，以约束安全主张，为系统卡、合规评估和国际安全机构提供治理启示。

**Link:**
https://arxiv.org/abs/2605.11496

5. **AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive**

**Publish Date:**
2026-05-13

**一句话总结:**
本文提出AutoLLMResearch框架，利用多保真度实验环境LLMConfig-Gym（包含超百万GPU时验证数据）训练研究代理，从低成本实验中学习通用原则，以高效自动化昂贵的大语言模型实验配置，在多种任务上展现良好的泛化能力。

**Link:**
https://arxiv.org/abs/2605.11518

6. **PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement**

**Publish Date:**
2026-05-13

**一句话总结:**
本文提出PIVOT框架，通过计划-检查-进化-验证四阶段和文本梯度信号，迭代优化代理的行动轨迹，以弥合大语言模型代理的计划与执行偏差，在DeepPlanning和GAIA上取得领先性能，且Token消耗比对比方法少3-5倍。

**Link:**
https://arxiv.org/abs/2605.11225

7. **Rethinking LLMOps for Fraud and AML: Building a Compliance-Grade LLM Serving Stack**

**Publish Date:**
2026-05-13

**一句话总结:**
本文针对欺诈检测和反洗钱领域的LLM服务需求，提出了一种基于vLLM等技术的合规级LLM服务栈，通过前缀缓存、动态批处理、推测解码等优化，将吞吐量提升至3600请求/小时，P99延迟降至6.4-8.7秒，并引入LLM-as-Judge质量门控确保输出合规性。

**Link:**
https://arxiv.org/abs/2605.11232

8. **Controllable User Simulation**

**Publish Date:**
2026-05-13

**一句话总结:**
针对对话智能体评估依赖可控用户模拟的问题，该研究将模拟形式化为因果推断任务，提出先验控制、分步动态控制和直接策略条件化训练方法，在标准基准上证实消除了前向偏差、保留了自然多样性并实现零样本泛化。

**Link:**
https://arxiv.org/abs/2605.11519

9. **Allegory of the Cave: Measurement-Grounded Vision-Language Learning**

**Publish Date:**
2026-05-13

**一句话总结:**
提出PRISM-VL，利用RAW格式测量数据结合曝光包围监督聚合训练视觉语言模型，在150K指令调优数据上比RGB基线提升BLEU、ROUGE-L和LLM-Judge准确率，改善低光等场景的推理。

**Link:**
https://arxiv.org/abs/2605.11727

10. **MIND-Skill: Quality-Guaranteed Skill Generation via Multi-Agent Induction and Deduction**

**Publish Date:**
2026-05-12

**一句话总结:**
MIND-Skill通过归纳与演绎两个智能体协作，利用重建损失、结果损失和评分损失联合优化生成高质量技能，在AppWorld和BFCL-v3上性能优于现有方法。

**Link:**
https://arxiv.org/abs/2605.08670
