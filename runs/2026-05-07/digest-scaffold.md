# Daily AI Info

## News

### 要闻

1. **Anthropic 与 SpaceX 合作新增 300MW 算力，放宽使用限制**

**摘要:**
Anthropic 宣布与 SpaceX 达成合作，获得 Colossus 1 数据中心全部超过 300 兆瓦的算力。 基于此及近期其他算力交易， Anthropic 即日上调使用限额： Claude Code 的五小时滚动速率限制翻倍。 同时移除 Pro 与 Max 方案在高峰时段的限额缩减。 API 中 Opus 模型速率限制也得到大幅提升。 值得注意的是，每周总体限额并未提升。

**Original Link:**
https://www.anthropic.com/news/higher-limits-spacex

### 模型发布

2. **豆包 Doubao-Seed-2.0-lite 模型升级支持全模态**

**摘要:**
字节火山 宣布 Doubao-Seed-2.0-lite 完成重大升级，成为 豆包 首款全模态理解模型。该模型支持视、图、音、文统一理解与跨模态推理，Agent、Coding与GUI能力增强，可闭环执行界面操作。 其视觉在物理、医疗推理上超越前代pro版，部分领域达SOTA；音频支持19语种转写互译。 该模型已在 火山方舟 上线。此外， Doubao-Seed-2.0-mini 同步上线，同样支持全模态。

**Original Link:**
https://mp.weixin.qq.com/s/nWOSnTKD07ORQGf54LQqKQ?scene=1&amp;click_id=8

3. **Zyphra发布ZAYA1-8B，AMD平台训练开源**

**摘要:**
Zyphra 发布了总参数 8.4B 、活跃参数 760M 的 MoE 语言模型 ZAYA1-8B 。 该模型完全在 AMD 集群上训练，在数学与编程推理任务上击败了部分大型模型。

**Original Link:**
https://www.zyphra.com/post/zaya1-8b

### 开发生态

4. **Claude Managed Agents 上线 dreaming 与 outcomes 等功能**

**摘要:**
Anthropic 为 Claude Managed Agents 推出预览版 dreaming 与测试版 outcomes 等功能。 其中， dreaming 可自动优化记忆实现 Agent 自我改进。 outcomes 可通过独立评分提升输出质量。

**Original Link:**
https://claude.com/blog/new-in-claude-managed-agents

5. **Cursor 发布 3.3 版，新增上下文占用明细及 CI 自动修复**

**摘要:**
Cursor 发布了 3.3 版本。开发者现在能直观查看上下文中 rules 、 skills 等内容的占用明细来优化配置。 该版本还能设置常驻 Agent 自动对 CI 失败提交修复。

**Original Link:**
https://x.com/cursor_ai/status/2052059748544249918

6. **TRAE 宣布三端同步全量免费开放**

**摘要:**
TRAE 宣布 SOLO 三端同步全量开放。 该产品支持通过移动端语音跨设备远程调度 Agent 任务，三端均可语音交互生成会议纪要。 桌面端与网页端新增 飞书 接入与定时任务功能。

**Original Link:**
https://solo.trae.cn/

7. **OpenClaw 发布 2026.5.5 及 5.6，新增功能并修复问题**

**摘要:**
OpenClaw 项目发布 2026.5.5 和 2026.5.6 两版更新。 2026.5.5 版修复了多平台频道与插件更新的稳定性问题。 2026.5.6 版则紧急修正了系列 Bug 与报错。

**Original Link:**
https://github.com/openclaw/openclaw/releases

8. **Warp 团队开源 oz-skills 集合，包含 15 个内部工作流技能**

**摘要:**
Warp 团队开源了包含 15 个组件的 Agent Skills 合集 oz-skills ，涵盖 Git 协作与 Web 审计等五大场景。 开发者可通过执行 npx 指令快速安装。

**Original Link:**
https://github.com/warpdotdev/oz-skills

### 产品应用

9. **谷歌更新搜索中AI Mode与AI Overviews，优化链接展示与排序**

**摘要:**
Google 更新了搜索中的 AI Mode 与 AI Overviews ，带来五项功能： AI 回答末尾提供延伸阅读建议；高亮展示用户订阅的新闻链接；引入社区观点预览；在正文旁直接嵌入相关链接；桌面端新增悬停链接预览。

**Original Link:**
https://blog.google/products-and-platforms/products/search/explore-web-generative-ai-search

10. **Manus 升级 Projects 功能，支持从任务中自动学习复用模式**

**摘要:**
Manus 为其 Projects 功能上线“从每个任务学习”能力。 该能力能自动识别任务中的可复用指令、文件与工作流。 经用户审查批准后，将更新项目上下文。

**Original Link:**
https://manus.im/blog/manus-projects-self-updating

### 技术与洞察

11. **Unsloth AI 联合 NVIDIA 优化，大模型训练速度提升约 25%**

**摘要:**
Unsloth AI 与 NVIDIA 联合发布技术指南，通过引入“打包序列元数据缓存”、“双缓冲检查点重载”以及" MoE 路由优化”三项技术，在 B200 显卡上将大语言模型训练速度提升约 25% 。

**Original Link:**
https://unsloth.ai/blog/nvidia-collab

12. **OpenAI 联合英伟达等开源 MRC 网络协议服务 AI 训练**

**摘要:**
OpenAI 联合 AMD 、 英伟达 等公司，通过开放计算项目正式开源了一种名为 MRC 的新型网络协议。 这个协议专为大规模 AI 训练设计，能解决同步训练时 GPU 数据传输的拥塞和故障问题。目前已在 Stargate 等项目中部署。

**Original Link:**
https://openai.com/index/mrc-supercomputer-networking/

### 行业动态

13. **Fenris Creations 宣布独立并联手 DeepMind 启动 AI Agent 研究**

**摘要:**
运营 EVE Online 的 CCP Games 正式更名为 Fenris Creations ，并与 Google DeepMind 达成合作。 双方将把该游戏作为安全沙盒，在受控离线环境中探索 AI Agent 的记忆、持续学习与长期规划能力。

**Original Link:**
https://www.eveonline.com/news/view/a-new-era

14. **谷歌 Flow Music 联手 Believe，向艺人开放 AI 音乐生成工具**

**摘要:**
Google 宣布与 Believe 达成合作，向其旗下艺人提供 AI 音乐生成工具 Flow Music 。 在此合作中， 谷歌 不主张对生成内容拥有所有权。

**Original Link:**
https://blog.google/innovation-and-ai/models-and-research/google-labs/believe-flow-music-partnership

15. **WorldClaw 联合特朗普家族 WLFI 平台推出 WorldRouter**

**摘要:**
近日， WorldClaw 与 特朗普 家族创立的加密项目 WLFI 联合推出模型路由平台 WorldRouter 。 用户凭单账户可调用超 300 款 AI 模型。 目前，社区对该平台折扣真实性及相关机制存在诸多质疑。

**Original Link:**
https://worldclaw.ai/

### 前瞻与传闻

16. **月之暗面传将获 20 亿美元融资，估值超 200 亿美元**

**摘要:**
据报道， Kimi 即将完成 20 亿美元 新一轮融资。 投后估值突破 200 亿美元 ，且该公司 ARR 已突破 2 亿美元 。

**Original Link:**
https://mp.weixin.qq.com/s/ThvJjPZfK1fF9rJJIIXSrg


## Paper

1. **Architectural Constraints Alignment in AI-assisted, Platform-based Service Development**

**Publish Date:**
2026-05-06

**一句话总结:**
这篇论文的核心贡献是：We propose a retrieval-augmented scaffolding approach that combines platform-based code generation with agentic clarification loops to expose and resolve architectural constraint ambiguities.

**Link:**
https://arxiv.org/abs/2605.04973

2. **Agentic Vulnerability Reasoning on Windows COM Binaries**

**Publish Date:**
2026-05-06

**一句话总结:**
这篇论文的核心贡献是：We present SLYP, an end-to-end agentic pipeline that discovers race condition vulnerabilities in COM binaries and generates debugger-verified proof-of-concept (PoC) code.

**Link:**
https://arxiv.org/abs/2605.05000

3. **Self-Induced Outcome Potential: Turn-Level Credit Assignment for Agents without Verifiers**

**Publish Date:**
2026-05-06

**一句话总结:**
这篇论文的核心贡献是：We propose Self-Induced Outcome Potential (SIOP), which treats semantic clusters of final answers as latent future outcome states for potential-based turn-level credit assignment.

**Link:**
https://arxiv.org/abs/2605.04984

4. **MRI-Eval: A Tiered Benchmark for Evaluating LLM Performance on MRI Physics and GE Scanner Operations Knowledge**

**Publish Date:**
2026-05-06

**一句话总结:**
这篇论文的核心贡献是：Purpose: We developed MRI-Eval, a tiered benchmark for relative model comparison on MRI physics and GE scanner operations knowledge using primary multiple-choice questions (MCQ), with stem-only and primed diagnostic conditions as complementary analyses.

**Link:**
https://arxiv.org/abs/2605.05175

5. **Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical System Prediction**

**Publish Date:**
2026-05-06

**一句话总结:**
提出 LaaB，把模型回答与自我判断之间的逻辑一致性建模成桥梁：一边利用内部特征的不确定性，一边利用显式 self-judgment 标签，再通过互学习融合两类信号来提升幻觉检测。

**Link:**
https://arxiv.org/abs/2605.05134

6. **Misaligned by Reward: Socially Undesirable Preferences in LLMs**

**Publish Date:**
2026-05-06

**一句话总结:**
这篇论文的核心贡献是：We introduce a framework that converts social evaluation datasets into pairwise preference data, leveraging gold labels where available and directional bias indicators otherwise.

**Link:**
https://arxiv.org/abs/2605.05003
