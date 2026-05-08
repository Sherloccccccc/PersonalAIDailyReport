# Daily AI Info

## News

### 要闻

1. **OpenAI 发布三款实时音频模型，GPT-Realtime-2 具 GPT-5 级推理**

**摘要:**
OpenAI 在 Realtime API 上线三款实时音频模型。 其中， GPT-Realtime-2 模型具备 GPT-5 级别推理能力，支持 128K 上下文与并行工具调用。 GPT-Realtime-Whisper 能提供低延迟流式转录。 GPT-Realtime-Translate 模型能实现超 70 种语言的实时翻译。 开发者可通过 API 直接集成它们来构建语音 Agent。

**Original Link:**
https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/

2. **火山方舟上线 Agent Plan 个人订阅套餐支持生成视频图片**

**摘要:**
火山方舟 正式上线面向个人用户的 Agent Plan 。 Agent Plan 提供最低 40 元/月 的四档套餐，主打 Agent 场景。 该方案采用 Agent 燃料值（AFP） 对不同模型按照不同费率计费，包含月额度、周额度和 五小时 额度限制。 套餐支持生成图片与视频，并限时附赠联网搜索额度。 该套餐额度仅供主流编程及 Agent 工具使用，严禁直接用于 API 调用。

**Original Link:**
https://www.volcengine.com/docs/82379/2366394?lang=zh

3. **Codex 上线 Chrome 扩展，新增 Vim 模式**

**摘要:**
Codex 推出 Chrome 扩展并发布更新。该扩展支持 Codex 在后台跨标签页并行处理 Web 任务。 同时， Codex 应用更新带来性能提升。新增 Vim 模式与键盘映射调试等功能。

**Original Link:**
https://developers.openai.com/codex/changelog#codex-2026-05-07

### 模型发布

4. **OpenAI 推出 GPT-5.5-Cyber 面向网络安全防御人员**

**摘要:**
OpenAI 推出了面向网络安全防御人员的 GPT-5.5-Cyber 模型，并同步通过 TAC 框架提供 GPT-5.5 模型。 从业人员可通过官网验证个人身份，或由企业联系官方代表申请访问权限。

**Original Link:**
https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/

5. **xAI 推出 Grok Imagine Quality Mode API**

**摘要:**
SpaceXAI 推出了 Grok Imagine Quality Mode API。 该模式提供高真实感的图像生成与编辑，能保持人物与物体一致性。

**Original Link:**
https://x.ai/news/grok-imagine-quality-mode

6. **Zyphra 发布 ZAYA1-74B-Preview，基于 AMD 硬件训练**

**摘要:**
Zyphra 发布了总参数 740亿 、激活参数 40亿 的混合专家模型 ZAYA1-74B-Preview 。 该模型基于 AMD 硬件端到端训练，未经过 RL 后训练和指令调优。 最终版预计 数周内 发布。

**Original Link:**
https://www.zyphra.com/post/zaya1-74b-preview

7. **Google 发布 Gemini 3.1 Flash-Lite 正式版，预览版本月下线**

**摘要:**
Google 发布了 Gemini 3.1 Flash-Lite 模型的正式版本。 Gemini API 中的预览版将于本月 25 日完全关闭。

**Original Link:**
https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available

### 开发生态

8. **Qoder CLI 发布 0.2.0 版本，重做交互层并预告开放 Agent SDK**

**摘要:**
Qoder CLI 发布 0.2.0 版本大升级，重做终端界面并加入 Vim 模式与可视化管理面板。 新版支持多模型灵活切换与手机远程控制。

**Original Link:**
https://mp.weixin.qq.com/s/NxIIAXwwPFZnQEZ49G8Y0A

9. **Amp 发布 CLI 重构版 Neo，支持远程控制与自动压缩**

**摘要:**
Amp CLI 正分批推送代号为 Neo 的重构版本。 新版支持网页端远程控制终端会话，上下文满 90% 自动压缩。 同时推出 Amp Plugin API 。

**Original Link:**
https://ampcode.com/news/neo

10. **Hermes Agent v0.13.0 发布，新增多 Agent 协作看板**

**摘要:**
Nous Research 发布了 Hermes Agent 版本更新。 此次核心引入持久化多 Agent 协作看板与跨轮次锁定目标的 goal 指令。 同时，团队集中修复了 八个 P0 级安全漏洞。 新版本还新增了可接入 Google Chat 的功能。

**Original Link:**
https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7

11. **OpenAI 开源 openai-cli 命令行工具映射 REST API 端点**

**摘要:**
OpenAI 在 GitHub 开源了官方命令行工具 openai-cli 。 该工具将 REST API 映射为 shell 命令，开发者配置环境变量后，即可在终端直接调用 API 。 这一举措能够快速实现 Agent 任务编排、图像语音生成与项目自动化管理。

**Original Link:**
https://github.com/openai/openai-cli

12. **OpenRouter 上线专用音频端点并发布统一网页搜索工具**

**摘要:**
OpenRouter 上线音频API与Web搜索抓取工具。 新增的 TTS 与 STT 专用端点汇聚多家模型，实现统一路由与计费。 Web工具允许支持工具调用的模型自主发起并发搜索，统一跨模型行为与结果。

**Original Link:**
https://openrouter.ai/docs/features/multimodal/tts

13. **strukto-ai 开源 Mirage 为 AI Agent 打造统一虚拟文件系统**

**摘要:**
strukto-ai 团队发布了面向 AI Agents 的开源虚拟文件系统 Mirage 。 该系统能将 S3 和 GitHub 等数十种云服务挂载为单一目录树， AI Agent 可直接使用 cat 、 grep 等标准 Unix 命令读写多种格式数据。

**Original Link:**
https://github.com/strukto-ai/mirage

### 产品应用

14. **OpenAI ChatGPT 推出可信联系人，人工审核防自残**

**摘要:**
OpenAI 在 ChatGPT 中推出了 Trusted Contact 可选安全功能，18 岁及以上用户可在设置中添加一位信任联系人。 当自动化系统与人工审核员检测到用户谈论自残时，会在一小时内向该联系人发送提醒。

**Original Link:**
https://openai.com/index/introducing-trusted-contact-in-chatgpt/

15. **千问 PC 端上线 AI 语音输入，免费开放支持跨应用调用**

**摘要:**
千问 的 PC 端应用免费上线了 AI 语音输入 功能。长按快捷键能在各类应用和网页中 转录语音 ，自动修正口误并做结构化整理。 双击快捷键还能唤醒 千问 AI 助手，通过语音直接完成复杂任务。

**Original Link:**
https://mp.weixin.qq.com/s/9Tkrvn8_741e01yBk2tKjA

16. **Anthropic 发布 Claude for Microsoft 365 插件正式版**

**摘要:**
Anthropic 正式发布 Claude for Microsoft 365 插件，其中 Excel 、 Word 和 PowerPoint 插件已转为正式版。 Outlook 进入公测。 所有付费套餐用户无需额外付费。

**Original Link:**
https://claude.com/claude-for-microsoft-365

17. **SpaceXAI 为 Grok 推出 Connectors，支持第三方应用集成**

**摘要:**
SpaceXAI 正式宣布为 Grok 推出 Connectors 功能，并已在网页端上线。 该功能深度集成了 Outlook 等第三方应用，能直接处理邮件、日历和文档等。

**Original Link:**
https://x.ai/news/grok-connectors

18. **Spotify 发布 save-to-spotify 开源工具 支持私人播客音频上传**

**摘要:**
Spotify 推出命令行工具 save-to-spotify 。 该工具支持通过 Agent 将本地或 AI 生成的音频上传至平台，并转为私人播客保存在个人库。

**Original Link:**
https://github.com/spotify/save-to-spotify

### 技术与洞察

19. **Anthropic 提出 Model Spec Midtraining 优化模型对齐泛化**

**摘要:**
Anthropic 的研究人员近日提出了一种名为 Model Spec Midtraining （MSM）的新方法。 通过在预训练后、对齐微调前使用合成文档训练模型学习其 Model Spec 的内容，从而塑造模型从后续对齐训练中的泛化方式。

**Original Link:**
https://alignment.anthropic.com/2026/msm/

20. **Anthropic 发布 NLA 方法揭示模型被评估意识**

**摘要:**
Anthropic 发布名为 Natural Language Autoencoders 的新研究，该方法能将 AI 模型内部的激活值转成可读文本。 该技术现已用于安全审计，成功揭示了模型未言明的隐藏心理。

**Original Link:**
https://www.anthropic.com/research/natural-language-autoencoders

21. **Anthropic 旗下 TAI 公布研究议程，聚焦经济安全四大领域**

**摘要:**
Anthropic 近日正式公布了旗下 The Anthropic Institute 的四大研究议程。 这四大议程涵盖经济扩散、威胁与韧性、真实环境中的 AI 系统、以及 AI 驱动的研发。 该计划旨在评估 AI 对社会的深层影响。

**Original Link:**
https://www.anthropic.com/research/anthropic-institute-agenda

22. **Anthropic 捐赠 Petri 对齐测试工具至 Meridian Labs**

**摘要:**
Anthropic 宣布将开源对齐测试工具 Petri 捐赠给非营利组织 Meridian Labs ，并发布 3.0 版本。 该工具通过独立的审计员与法官模型，专门测试大语言模型是否存在欺骗或配合有害请求等不良倾向。

**Original Link:**
https://www.anthropic.com/research/donating-open-source-petri

23. **OpenAI 披露多款 GPT-5 模型训练意外评分思维链**

**摘要:**
OpenAI 发布博客介绍其发现 GPT-5.4 等多个模型在强化学习训练中意外对思维链进行了评分。 消融实验表明该情况未对 CoT 可监控性造成实质性损害，团队已修复相关奖励通路并扩展了自动检测系统。

**Original Link:**
https://alignment.openai.com/accidental-cot-grading

24. **腾讯混元开源 OpenSearch-VL 多模态深度搜索训练方案**

**摘要:**
腾讯混元 等机构开源了多模态深度搜索 Agent 训练方案 OpenSearch-VL 。 该方案提供从数据管道到致命感知强化学习算法的完整实现。

**Original Link:**
https://github.com/shawn0728/OpenSearch-VL

25. **Goodfire 发布神经几何学研究**

**摘要:**
Goodfire 发布“神经几何学”研究，认为神经网络内部充满弯曲的几何流形。 沿流形干预能实现模型平滑操控与精准解读，避免传统线性方法造成的输出混乱。

**Original Link:**
https://www.goodfire.ai/research/the-world-inside-neural-networks

26. **Mozilla 披露借助Claude Mythos Preview 修复漏洞数超过去十五个月总和**

**摘要:**
Mozilla Firefox 团队发文称，今年 4月 借助 Claude Mythos Preview 模型，成功修复了 423 个安全漏洞。 这一数量超过了此前 15个月 的总和。其中该模型直接发现 271 个漏洞。

**Original Link:**
https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/

27. **Google DeepMind 展示 AlphaEvolve 一年间成果**

**摘要:**
Google DeepMind 发文介绍了其此前推出的 AI Agent AlphaEvolve ，在过去一年中取得的显著成效。 该系统在推动社会影响方面展现了重要作用，并在加速研究前沿领域发挥了关键驱动能力。 同时，它成功实现了 AI 基础设施的优化，为技术落地提供了坚实基础。 此外， AlphaEvolve 还在规模化商业应用等多个维度上取得了突破性进展。

**Original Link:**
https://deepmind.google/blog/alphaevolve-impact/

### 行业动态

28. **xAI 并入 SpaceX，更名为 SpaceXAI**

**摘要:**
马斯克 在社交平台 X 上宣布，旗下 xAI 不再独立运营。 该公司将整体并入 SpaceX 。 并正式更名为 SpaceXAI 。

**Original Link:**
https://x.com/elonmusk/status/2052105373621121284

29. **Anthropic 在 HackerOne 平台公开漏洞赏金计划**

**摘要:**
Anthropic 正式在 HackerOne 平台向公众开放安全漏洞赏金计划。 研究者可通过该平台提交基础设施或者代码层面的漏洞报告获取最高 一万美元 赏金。

**Original Link:**
https://hackerone.com/anthropic

30. **DeepL 裁员 250 人，转型 AI 原生公司布局语音翻译**

**摘要:**
DeepL 宣布裁减约 250 个岗位，以转型为 AI 原生企业。 同时该公司通过收购音频流媒体技术公司 Mixhalo 团队，将战略重点转向实时语音翻译领域。

**Original Link:**
https://the-decoder.com/ai-translation-company-deepl-cuts-around-250-jobs-to-rebuild-as-an-ai-native-organization/


## Paper

1. **SkillOS: Learning Skill Curation for Self-Evolving Agents**

**Publish Date:**
2026-05-07

**一句话总结:**
SkillOS 提出一种基于强化学习的技能管理方法，通过冻结执行器与可训练管理器的协作，从任务流中学习维护外部技能库，使智能体在多轮交互中自我进化，其技能最终组织为富含元技能的 Markdown 结构化文件，提升了长期任务效率。

**Link:**
https://arxiv.org/abs/2605.06614

2. **EMO: Pretraining Mixture of Experts for Emergent Modularity**

**Publish Date:**
2026-05-07

**一句话总结:**
提出EMO预训练方法，通过限制同文档token共享专家池，使MoE模型在仅使用25%专家时精度仅降1%，且专家按数学、代码等语义领域分工，为稀疏模型的模块化高效部署开辟了新路径。

**Link:**
https://arxiv.org/abs/2605.06663

3. **StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction**

**Publish Date:**
2026-05-07

**一句话总结:**
StraTA框架为LLM智能体强化学习引入轨迹级策略，通过层次GRPO联合训练策略与动作，在ALFWorld、WebShop和SciWorld上成功率分别达93.1%、84.2%和63.5%，超越前沿闭源模型。

**Link:**
https://arxiv.org/abs/2605.06642

4. **Superintelligent Retrieval Agent: The Next Frontier of Information Retrieval**

**Publish Date:**
2026-05-07

**一句话总结:**
SIRA通过LLM离线扩充文档检索词、在线预测查询缺失词汇并结合文档频率过滤，将多轮探索搜索压缩为单次加权BM25检索，在十个BEIR基准上超越稠密检索与多轮代理方法，实现高效、可解释的检索。

**Link:**
https://arxiv.org/abs/2605.06647

5. **STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?**

**Publish Date:**
2026-05-07

**一句话总结:**
针对LLM代理记忆中隐式冲突导致信念过时问题，提出包含400个场景的STALE基准和CUPMem原型，从状态解析、前提抵抗和隐式策略适应三维度评估发现模型准确率仅55.2%，揭示检索更新证据与基于证据行动间的差距。

**Link:**
https://arxiv.org/abs/2605.06527

6. **Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents**

**Publish Date:**
2026-05-07

**一句话总结:**
提出首个结构化来源归因评测框架，通过AST解析LLM生成报告中的内联引用并检索原文，从链接可访问性、内容相关性和事实准确性三维度评估14个模型，发现事实准确率仅39-77%且随检索轮次增加而下降。

**Link:**
https://arxiv.org/abs/2605.06635

7. **MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems**

**Publish Date:**
2026-05-07

**一句话总结:**
MASPO框架通过联合评价机制评估提示词对下游代理成功的影响，无需标签，采用进化束搜索迭代优化多代理系统提示，在6项任务上平均提升2.9个点，开源代码，解决本地目标与全局目标错位问题。

**Link:**
https://arxiv.org/abs/2605.06623

8. **Algospeak, Hiding in the Open: The Trade-off Between Legible Meaning and Detection Avoidance**

**Publish Date:**
2026-05-07

**一句话总结:**
该论文通过构建可调的 Algospeak 变体数据集，并利用七种语言模型评估语义可恢复性与虚假信息检测之间的权衡，提出了多数可理解调制（MUM）概念，为对抗性语言规范研究提供了框架。

**Link:**
https://arxiv.org/abs/2605.06619

9. **How Many Iterations to Jailbreak? Dynamic Budget Allocation for Multi-Turn LLM Evaluation**

**Publish Date:**
2026-05-07

**一句话总结:**
提出动态预算分配框架DAPRO，通过预测优化与覆盖保证，在多轮LLM交互中高效估计越狱等事件所需迭代次数的下界，并在Llama 3.1等模型上验证了其在安全和幻觉检测任务中的有效性。

**Link:**
https://arxiv.org/abs/2605.06605

10. **Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study**

**Publish Date:**
2026-05-07

**一句话总结:**
提出多模态域泛化统一基准MMDG-Bench，涵盖6个数据集、三种任务和多种评估设置，发现现有方法相比ERM基线提升有限，且在损坏与缺失模态下性能大幅下降，距上界性能仍有较大差距。

**Link:**
https://arxiv.org/abs/2605.06643
