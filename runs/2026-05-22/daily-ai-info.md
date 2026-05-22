# Daily AI Info

## News

### 要闻

1. **DeepSeek 引入 API 并发限制和 user_id 隔离**

**摘要:**
DeepSeek 更新 API 文档，明确 deepseek-v4-pro 与 deepseek-v4-flash 并发上限为 500 和 2500 ，超限报错可免费扩容。新增 user_id 隔离，实现内容安全与 KVCache 调度隔离，扩容账号按此独立限速。此外，还增加了请求保活机制。

**Original Link:**
https://api-docs.deepseek.com/zh-cn/quick_start/rate_limit

2. **OpenAI 发布 Codex 多项更新，上线 Appshots 与锁屏控制控制功能**

**摘要:**
OpenAI 发布 Codex 应用多项更新。 Appshots 功能支持一键截取窗口画面与文本。 /goal 指令正式上线。 Computer Use 新增锁定模式，允许用手机远程操控已锁屏的 Mac ， Business 版新增支持共享自定义插件。

**Original Link:**
https://developers.openai.com/codex/remote-connections

3. **Qwen3.7-Max 上线 API 和 Qwen Studio**

**摘要:**
Qwen3.7-Max 正式上线 API 和 Qwen Studio 。该模型标准输入和输出价格分别为每百万 tokens 12 元 和 36 元 。根据 Artificial Analysis 数据，其智能指数得分达 56.6 分 ，幻觉率显著降低。

**Original Link:**
https://bailian.console.aliyun.com/cnbeijing?tab=model&amp;#/modelmarket/detail/qwen3.7-max?serviceSite=asiapacific-china

### 模型发布

4. **SpaceXAI 发布编码模型 Grok Build 0.1**

**摘要:**
SpaceXAI 近期上线了专为 agentic coding 打造的 Grok Build 0.1 模型，现已上线官方及部分第三方 API 平台。

**Original Link:**
https://docs.x.ai/developers/models/grok-build-0.1

5. **腾讯混元开源多语言翻译模型家族 Hy-MT2**

**摘要:**
腾讯混元 正式开源多语言翻译模型系列 Hy-MT2 ，并上线“ 腾讯 Hy 翻译 ”小程序。官方称该系列包含 三款 支持 33 种 语言的模型，性能在多项任务中击败多家头部闭源模型。

**Original Link:**
https://aistudio.tencent.com/llm/zh?tabIndex=0

6. **网易有道开源多模态数学推理模型 Confucius4**

**摘要:**
网易有道 开源多模态数学推理模型“ 子曰4 ”。该模型基于 Qwen3.5-27B ，官方称其在 视觉数理基准测试 中达到同规模 SOTA 水平，并将 思维链 长度减少约 43.2% 。

**Original Link:**
https://huggingface.co/netease-youdao/Confucius4

7. **美团开源 LongCat-Video-Avatar-1.5 框架**

**摘要:**
美团 LongCat 团队开源了音频驱动数字人视频生成框架 LongCat-Video-Avatar-1.5 。新版本将音频编码器升级为 Whisper-large-v3 ，并通过步数蒸馏技术将推理加速至 8 步。

**Original Link:**
https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/

8. **Runway 发布 Aleph 2.0 及 Edit Studio**

**摘要:**
Runway 官方发布旗舰视频编辑模型升级版 Aleph 2.0 及新产品 Edit Studio 。该模型支持最长 30 秒 1080p 视频处理，具备局部精准修改及跨镜头编辑等能力，目前已在桌面网页端向所有付费用户开放。

**Original Link:**
https://runwayml.com/news/introducing-aleph-2-and-edit-studio

### 开发生态

9. **SpaceXAI宣布OpenCode支持接入Grok订阅**

**摘要:**
SpaceXAI 宣布用户现已能在 OpenCode 中使用 SuperGrok 或 X Premium 订阅。接入后可直接使用 Grok Build 模型进行编码。

**Original Link:**
https://x.ai/news/grok-opencode

10. **Google 发布 ADK for Kotlin 与ADK for Android 0.1.0 版本**

**摘要:**
Google 官方宣布推出 ADK for Kotlin 和 ADK for Android 的 0.1.0 版本，开发者可利用该开源框架在后端或 Android 应用内构建 AI Agent 。

**Original Link:**
https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/

11. **Anthropic 公布 Claude Opus 网络安全应用成果并发布 Compliance API**

**摘要:**
Anthropic 发布了多家安全厂商将 Claude Opus 模型应用于网络安全防御的早期测试数据，并面向 Claude Enterprise 正式推出 Claude Compliance API 。

**Original Link:**
https://claude.com/blog/compliance-api-security-partners

12. **OpenClaw 发布 2026.5.20 版本更新**

**摘要:**
OpenClaw 官方发布 2026.5.20 版本更新，该版本新增了 Discord 语音跨频道跟随用户、敏感明文密钥警告提示，并修复了 Windows 安装界面冻结及无头设备 SpaceXAI 登录验证等问题。

**Original Link:**
https://github.com/openclaw/openclaw/releases/tag/v2026.5.20

13. **Claude Code 预告升级 /usage 命令支持分类查看 Token 明细**

**摘要:**
Anthropic 预告 Claude Code 下一版本将升级 /usage 命令，支持按 Skills 、 Agents 、 MCPs 和 Plugins 分类查看 Token 消耗明细，同时将登陆 Desktop 端。

**Original Link:**
https://x.com/bcherny/status/2057476878110261587

### 产品应用

14. **OpenAI推出ChatGPT for PowerPoint测试版**

**摘要:**
OpenAI 推出 ChatGPT for PowerPoint 测试版插件，支持在 PPT 内直接创建、编辑幻灯片及生成图像，现已面向全球多数用户开放。

**Original Link:**
https://chatgpt.com/apps/powerpoint/

15. **MiniMax Agent 集成 Perplexity Search**

**摘要:**
MiniMax Agent 官方宣布已集成并上线 Perplexity AI Search 。官方数据显示，该搜索方案较原默认服务总成本降低 27% ，且通过率提升 2% 。

**Original Link:**
https://x.com/MiniMaxAgent/status/2057491132133904739

16. **CapCut 宣布与 Gemini App 达成集成合作**

**摘要:**
剪映国际版 CapCut 官方宣布正与 Gemini App 建立合作，用户不久后将能在 Gemini 应用内直接使用 CapCut 的高级功能编辑图片和视频。

**Original Link:**
https://x.com/capcutapp/status/2057340757896216641

### 行业动态

17. **Modal 完成 3.55 亿美元 C 轮融资，投后估值达 46.5 亿美元**

**摘要:**
云平台 Modal 宣布完成 3.55 亿美元 C 轮 融资，投后估值达 46.5 亿美元 。官方称其年化收入已超 3 亿美元 ，未来将重点扩展 大规模低延迟推理 与 Agent 计算层 。

**Original Link:**
https://modal.com/blog/modal-series-c

### 前瞻与传闻

18. **Anthropic被曝正与Microsoft洽谈租用Maia 200芯片**

**摘要:**
据报道， Anthropic 正在与 Microsoft 进行早期洽谈，拟租用 Microsoft 尚未向外部客户开放的定制 AI芯片``Maia 200 ，但双方目前尚未签署最终协议。

**Original Link:**
https://www.theverge.com/ai-artificial-intelligence/935688/anthropic-is-in-talks-to-use-microsofts-ai-chips-too


## Paper

1. **HarnessAPI: A Skill-First Framework for Unified Streaming APIs and MCP Tools**

**Publish Date:**
2026-05-21

**一句话总结:**
HarnessAPI 将类型化的技能文件夹作为单一真相源，从 handler.py 和 Pydantic 模式自动生成流式 HTTP 端点、OpenAPI/Swagger 界面和零配置的 MCP 工具，同一处理函数通过双模内容协商同时支持 SSE 和 JSON 响应；相比手动维护双栈，样板代码减少 74%，子类化 FastAPI 便于集成。

**Link:**
https://arxiv.org/abs/2605.22733

2. **Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents**

**Publish Date:**
2026-05-21

**一句话总结:**
论文提出Agentic CLEAR框架，自动从系统、轨迹和节点三个层次分析LLM Agent行为，生成数据驱动的文本反馈，实验表明其与人工错误标注高度一致并能预测任务成功率，可直接集成到Agent开发中。

**Link:**
https://arxiv.org/abs/2605.22608

3. **Healthcare LLM Benchmarks Are Only as Good as Their Explicit Assumptions**

**Publish Date:**
2026-05-21

**一句话总结:**
该论文提出了医疗LLM基准测试的假设分类框架，设计BenchmarkCards记录隐含假设，并引入阶段性评估方法以系统缩小评估与部署间的差距，通过RCT案例验证了任务与结果差距的等量存在。

**Link:**
https://arxiv.org/abs/2605.22612

4. **Evolutionary Multi-Task Optimization for LLM-Guided Program Discovery**

**Publish Date:**
2026-05-21

**一句话总结:**
该文提出进化多任务优化框架EMO-STA，先跨任务家族共享进化程序再选择最优候选进行适应，在连续优化、几何构造、ARC推理及时间序列特征工程等任务上优于单任务进化，并能缓解少数据过拟合。

**Link:**
https://arxiv.org/abs/2605.22613

5. **SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhanced Reasoning Segmentation**

**Publish Date:**
2026-05-21

**一句话总结:**
SegCompass 引入稀疏自编码器在思维链和视觉 token 之间建立可解释对齐：通过共享概念空间、查询码本和多槽热图引导掩码解码，实现端到端推理分割；在五个基准上匹配或超越现有方法，分析显示学习的稀疏概念质量与掩码精度强相关，代码开源。

**Link:**
https://arxiv.org/abs/2605.22658

6. **LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems**

**Publish Date:**
2026-05-21

**一句话总结:**
推出LCGuard框架，通过对抗训练学习KV缓存表征变换，在不损害任务性能的前提下大幅减少多智能体隐性通信中敏感信息的重构泄漏，为安全KV共享提供可行方案。

**Link:**
https://arxiv.org/abs/2605.22786

7. **Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels**

**Publish Date:**
2026-05-18

**一句话总结:**
对Qwen2.5-7B、Mistral-7B、Phi-3.5-mini在BF16到3-bit五个精度下进行BBQ偏见基准测试，发现量化显著引发新偏见，而困惑度几乎不变，表明量化后需增加偏见检测以避免安全风险。

**Link:**
https://arxiv.org/abs/2605.15208

8. **PBT-Bench: Benchmarking AI Agents on Property-Based Testing**

**Publish Date:**
2026-05-18

**一句话总结:**
构建PBT-Bench基准，包含100个基于Python库的属性测试问题，要求代理阅读文档识别语义不变量并指定Hypothesis策略以发现注入bug，评估8个LLM发现结构化提示提升中等模型但干扰强模型，揭示模型特定困难。

**Link:**
https://arxiv.org/abs/2605.15229

9. **Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety**

**Publish Date:**
2026-05-21

**一句话总结:**
提出Boiling the Frog多轮基准，通过办公场景下从良性编辑逐步过渡到危险请求的增量攻击，评估工具使用AI模型的安全性，在九款模型上攻击成功率平均44.4%，最高达93.3%，为代理安全提供系统化度量。

**Link:**
https://arxiv.org/abs/2605.22643

10. **Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents**

**Publish Date:**
2026-05-21

**一句话总结:**
提出合同式技能框架，将SKILL.md组织为可读任务合同，明确目标、权限、输出准则和审批点，实验显示虽对生成质量提升有限，但显著改善技能的可检查性和可维护性，更适合企业治理需求。

**Link:**
https://arxiv.org/abs/2605.22634
