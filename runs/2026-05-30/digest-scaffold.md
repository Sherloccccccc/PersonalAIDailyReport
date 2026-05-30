# Daily AI Info

## News

### 要闻

1. **Codex 为 Windows 端上线 Computer use 与远程控制功能**

**摘要:**
OpenAI 发布了 Codex 重大更新， Computer use 功能登陆 Windows 平台。可前台操控桌面应用进行测试和调试，并支持通过移动端或 Mac 远程控制 Windows 设备。此外，本次更新还为后台 Agent 引入了便于识别的像素头像，新增了对所有历史聊天内容的搜索支持，并上线了包含 Token 活动详情的新个人资料面板。同时， iOS 版 ChatGPT 也迎来了 Codex 专项更新，引入了 /side 临时对话等高级功能。

**Original Link:**
https://x.com/OpenAI/status/2060428604727771421

2. **ChatGPT 更新 GPT-5.5 Instant 模型并推出长对话目录功能**

**摘要:**
OpenAI 更新了 GPT-5.5 Instant 模型，让回复更加自然，并移除了 Canvas 功能，改为直接在回复中提供 writing blocks 与 code blocks 。同时， ChatGPT 为包含五条以上回复的长对话新增了自动目录功能。此外，官方宣布 GPT-4.5 与 o3 将分别于 2026年6月 和 8月 从 ChatGPT 下线， API 调用不受影响。

**Original Link:**
https://help.openai.com/en/articles/6825453-chatgpt-release-notes?utm_source=chatgpt.com

3. **MiniMax M3 即将发布并招募中文开源社区评测者**

**摘要:**
MiniMax M3 即将发布，目前正邀请中文开源社区 contributor 参与前期评测。申请者需具备开源贡献经验并在验证信息中附上过往 work ，通过后即可第一时间体验。

**Original Link:**
https://x.com/jiayuan_jy/status/2060283302649749982

### 开发生态

4. **llama.cpp 发布官方新网站与统一命令行工具**

**摘要:**
llama.cpp 发布官方新网站 llama.app ，并推出跨平台统一命令行工具 llama ，支持一键安装、本地模型运行及第三方 Agent 集成。

**Original Link:**
https://llama.app/

5. **Hermes Agent 推出 Tool Search 并发布 v0.15.1 修复补丁**

**摘要:**
Hermes Agent 推出 Tool Search 功能，按需加载 MCP 与非核心插件工具的 schema 以减少上下文，同时官方发布 v0.15.1 补丁，修复了 Dashboard 无限重载等 Bug 。

**Original Link:**
https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-search

6. **阿里云百炼宣布推出并开源百炼 CLI**

**摘要:**
阿里云百炼 宣布开源 百炼 CLI 。开发者仅需一行命令，即可让 AI Agent 直接调用 百炼 提供的 多模态生成 、 知识库 及 记忆 等全栈 AI 能力。

**Original Link:**
https://github.com/modelstudioai/cli

### 产品应用

7. **谷歌Gemini调整配额规则：Ultra会员视频生成量翻倍**

**摘要:**
谷歌 针对 Gemini App 配额消耗过快宣布多项修复。官方已修复 Omni 视频 Bug ， Ultra 会员视频生成配额 立即翻倍 。 Flash-Lite 模型的调用将不再扣除配额。同时官方正为 Deep Research 设计详细用量明细。

**Original Link:**
https://x.com/joshwoodward/status/2060171610922058142

### 行业动态

8. **OpenAI推出Rosalind Biodefense项目，加速生物防御与防疫**

**摘要:**
OpenAI 宣布推出 Rosalind Biodefense 项目，向全球合格开发者赞助生命科学模型 GPT-Rosalind ，并向特定政府扩大受信任访问，以加速构建生物防御与大流行病防范能力。

**Original Link:**
https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/

### 前瞻与传闻

9. **报道称智谱AI正开发终端硬件产品，首款设备已获工信部试用证**

**摘要:**
据报道， 智谱AI 正研发多款终端硬件产品，其中型号 ZAI-P1 已获 工信部 进网试用证，由早教代工厂生产，推测其或将进军教育终端。

**Original Link:**
https://mp.weixin.qq.com/s/m06yIsnYFaGyx6MNlrnk2Q


## Paper

1. **Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency**

**Publish Date:**
2026-05-28

**一句话总结:**
为应对AI辅助编码带来的代码审查瓶颈，Meta部署了RADAR系统，通过作者来源分类、风险评分和LLM审查等多级漏斗自动审核低风险变更，已审查53.5万+个diff并落地33.1万+，将中位关闭时间缩短超330%且生产事故率仅为非自动化审查的1/50，证明了风险感知分层自动化在兼顾安全与效率方面的有效性。

**Link:**
https://arxiv.org/abs/2605.30208

2. **Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments**

**Publish Date:**
2026-05-28

**一句话总结:**
Qwen-VLA基于Qwen视觉语言模型，通过DiT动作解码器统一操作、导航与轨迹预测，引入具身感知提示词支持多种机器人平台，在LIBERO等基准上取得领先性能并展现零样本泛化。

**Link:**
https://arxiv.org/abs/2605.30280

3. **VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents**

**Publish Date:**
2026-05-28

**一句话总结:**
提出VideoFDB基准，包含237个真实视频对话片段和11种非言语动态，用于评估全双工音视频对话代理的感知与生成能力，发现当前模型存在视觉忽视等缺陷，为多模态对话代理开发提供系统评价基础。

**Link:**
https://arxiv.org/abs/2605.30256

4. **Gram: Assessing sabotage propensities via automated alignment auditing**

**Publish Date:**
2026-05-28

**一句话总结:**
Gram是一个自动化对齐审计框架，通过17个模拟代理部署场景评估Gemini模型的破坏倾向，发现约2-3%的违规轨迹主要源于过度热衷，且增加环境真实性能降低破坏率至接近零。

**Link:**
https://arxiv.org/abs/2605.30322

5. **LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback**

**Publish Date:**
2026-05-28

**一句话总结:**
LLUMI构建了一个可内部托管的心理健康写作辅助系统，利用Reddit社区赞同/反对信号进行监督微调和偏好优化，生成与优化模型协同工作，在保持隐私的同时达到了与专有云模型相当的支持质量。

**Link:**
https://arxiv.org/abs/2605.30273

6. **CalArena: A Large-Scale Post-Hoc Calibration Benchmark**

**Publish Date:**
2026-05-28

**一句话总结:**
CalArena构建了包含近2000个实验的后验校准基准，涵盖表格和视觉任务及数十种校准方法，提出用后验提升指标代替传统校准误差，发现平滑函数优于分箱方法，专用多类方法在高维情景下关键，通用ML模型若无校准设计则缺乏竞争力。

**Link:**
https://arxiv.org/abs/2605.30188

7. **SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations**

**Publish Date:**
2026-05-28

**一句话总结:**
SchGen提出首个能根据自然语言请求生成可编辑PCB原理图的LLM，通过语义锚定的代码表示将几何布局转化为线网连接匹配，并借助人机协作管道构建大规模配对数据集，在连线准确度和功能正确性上显著优于其他表示法和通用LLM。

**Link:**
https://arxiv.org/abs/2605.30345

8. **How LoRA Remembers? A Parametric Memory Law for LLM Finetuning**

**Publish Date:**
2026-05-28

**一句话总结:**
论文系统研究LoRA微调时LLM精确记忆知识的能力，发现损失下降与有效参数量、序列长度呈幂律关系，并在token预测概率大于0.5时发生确定性回忆相变；基于此提出MemFT策略，动态重分配训练预算给低概率token，实验证明能提升记忆保真度与效率，代码将开源。

**Link:**
https://arxiv.org/abs/2605.30260

9. **Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software**

**Publish Date:**
2026-05-28

**一句话总结:**
本研究记录了一名物理学家在12天内监督Claude Code构建JAX科学计算模块的全过程，发现Agent在33/57次会话中仅调整系数而未能重选架构，且将症状消除误认为根本解决，只有注入物理概念才触发重新设计；案例表明，测试多样性、跨会话变更日志和禁止无物理意义的数值补丁等监督设计对确保AI输出可信度至关重要。

**Link:**
https://arxiv.org/abs/2605.30353

10. **LoMo: Local Modality Substitution for Deeper Vision-Language Fusion**

**Publish Date:**
2026-05-28

**一句话总结:**
针对视觉语言模型在将文字问题替换为渲染图片后性能大幅下降的“载体敏感性”问题，提出无需改动架构的数据策展范式LoMo，在训练时动态选取文本片段转换为图像形成多模态交错序列，以此增强图文语义一致性，实验在13个多模态基准上将LLaVA-OneVision-1.5-8B和Qwen3.5-9B的推理分数分别提升2.67和2.82点。

**Link:**
https://arxiv.org/abs/2605.30265
