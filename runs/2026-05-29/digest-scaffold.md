# Daily AI Info

## News

### 要闻

1. **Anthropic 发布 Claude Opus 4.8 模型**

**摘要:**
Anthropic 发布 Claude Opus 4.8 模型，强化了编码、Agent任务及长时运行工作的一致性方面的能力。该模型现已在官方全平台和各类第三方平台上线，官方 API 定价不变 ， Fast 模式 降价三分之二 且 提速约2.5倍 。同步面向 claude.ai 和 Cowork 的所有用户推出 推理努力程度控制 功能。 Anthropic 还表示正开发更低成本同等能力模型，同时预计 数周内 将 Mythos 级别模型推向所有客户。

**Original Link:**
https://www.anthropic.com/news/claude-opus-4-8

2. **Claude Code 推出 dynamic workflows 研究预览，支持数百 subagent 并行编排**

**摘要:**
Anthropic 发布 Claude Code 更新，上线 dynamic workflows 功能与 Opus 4.8 模型。 workflows 可调度 上千个 subagent 并行处理 大规模任务 ，同时 Opus 4.8 的 fast mode 能以 两倍价格 换取约 2.5倍 速度。

**Original Link:**
https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

3. **Anthropic 完成 650 亿美元 H 轮融资，投后估值达 9650 亿美元**

**摘要:**
Anthropic 宣布完成 650 亿美元 H 轮 融资，投后估值达 9650 亿美元 。这笔资金预计将用于推进 安全 与 可解释性 研究，并扩展 算力 满足对 Claude 的需求。

**Original Link:**
https://www.anthropic.com/news/series-h

4. **阶跃星辰开源 Step 3.7 Flash 多模态推理模型**

**摘要:**
阶跃星辰 发布 Step 3.7 Flash 多模态推理模型，采用 198B 稀疏 MoE 架构且仅激活约 11B 参数，支持多档推理努力程度，已开放 API 调用并以 Apache 2.0 协议开源全部权重。

**Original Link:**
https://static.stepfun.com/blog/step-3.7-flash/

### 模型发布

5. **PaddlePaddle 推出 PaddleOCR-VL 1.6 升级文档解析能力**

**摘要:**
PaddlePaddle 正式发布 PaddleOCR-VL 1.6 模型。官方称其在 OmniDocBench v1.6 基准达到 96.33% ，且架构兼容前代，支持即插即用。

**Original Link:**
https://x.com/PaddlePaddle/status/2059990434827661769

6. **商汤开源 SenseNova-U1-8B-MoT-Infographic 模型**

**摘要:**
商汤 发布并开源了 SenseNova-U1-8B-MoT-Infographic 模型。官方称该模型提升了高密度信息图的文字准确率与排版稳定性，在相关基准测试中达到开源 SOTA 水平。

**Original Link:**
https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-Infographic

7. **Liquid AI 发布 LFM2.5-8B-A1B 设备端模型**

**摘要:**
Liquid AI 发布 LFM2.5-8B-A1B 模型。该模型具有 128K 上下文，官方称其性能可媲美参数量大 4 倍的同类 MoE 模型。

**Original Link:**
https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF

8. **Bagel Labs 发布 Paris 2.0 去中心化视频生成模型**

**摘要:**
Bagel Labs 团队发布了 Paris 2.0 视频生成模型。官方称这是首个去中心化训练视频生成模型。该模型权重已在 Hugging Face 上有限度开放。

**Original Link:**
https://huggingface.co/bageldotcom/paris2

9. **ElevenLabs 推出支持 90 多种语言的 Dubbing v2**

**摘要:**
ElevenLabs 发布了 Dubbing v2 配音模型。该模型直接处理原始音频，能在 90 多种语言的翻译中保留原说话人的情感、语气和声音特征，并通过 同步感知逻辑 实现配音精准对齐。

**Original Link:**
https://elevenlabs.io/dubbing-studio

10. **ElevenLabs 发布 Music v2 模型，支持跨流派无缝转换与局部重绘**

**摘要:**
ElevenLabs 近期发布了 Music v2 音乐模型，支持在同一首歌内无缝融合歌剧与重金属风格，并新增局部重绘功能，现已正式上线。

**Original Link:**
https://elevenlabs.io/blog/introducing-music-v2

11. **Nano Banana 系列模型 GA，可通过 Gemini API 投入生产使用**

**摘要:**
Google 宣布将 Nano Banana Pro 和 Nano Banana 2 两款图像生成模型正式转为GA，现可通过 Gemini API 投入生产环境使用。

**Original Link:**
https://x.com/googleaidevs/status/2060068093485895978

### 开发生态

12. **Antigravity CLI 1.0.3 发布：支持配额耗尽后使用 Google AI credits**

**摘要:**
Antigravity CLI 发布 1.0.3 版。该版本新增配额耗尽时启用 Google AI credits 的功能，同时改进了 /diff 体验并修复多项关键问题。

**Original Link:**
https://x.com/shengzheyao/status/2059814938609332726

13. **腾讯混元发布 Hy-Memory 插件提升 Agent 长期记忆能力**

**摘要:**
腾讯混元 正式发布专为 Openclaw 等长期协作型 Agent 打造的 Hy-Memory 记忆插件，官方称其通过 6层记忆框架 与 演化链技术 解决记忆碎片化问题。

**Original Link:**
https://memory.hunyuan.tencent.com/

14. **Firecrawl 发布 Monitoring 网页变更监控功能**

**摘要:**
Firecrawl 发布 Monitoring 功能，系统在网页变动时仅提取变化并通知 Agent ，官方称最高减少 90% 的 LLM token 消耗。

**Original Link:**
https://x.com/firecrawl/status/2060042535003701523

15. **Nous Research 发布 Hermes Agent v0.15.0 版本**

**摘要:**
Nous Research 官方发布 Hermes Agent v0.15.0 版本，新增对 Opus 4.8 等模型的支持及 SpaceXAI 集成，官方称其会话搜索速度提升达 750 倍。

**Original Link:**
https://x.com/Teknium/status/2060088572049559893

16. **OpenClaw 更新 v2026.5.27：官方称包体积缩小 59%，强化安全边界**

**摘要:**
OpenClaw 发布 2026.5.27 版本，官方称其稳定冷启动 Agent 轮次提速 2.9 倍，发布包体积缩小 59% ，同时收紧运行时安全边界。

**Original Link:**
https://openclaw.ai/blog/lighter-core-sharper-claws/

### 产品应用

17. **Perplexity AI 助手 Computer 上线插件接入 Microsoft 365**

**摘要:**
Perplexity AI 宣布其产品 Computer 集成至 Microsoft 365 。用户可在 Word 、 Excel 等应用内直接起草、分析与联网搜索，插件已上架 微软应用商店 。

**Original Link:**
https://www.perplexity.ai/hub/products/integrations/microsoft

18. **微软重构 Microsoft 365 Copilot 并提升加载速度**

**摘要:**
微软 近日重构 Microsoft 365 Copilot 。官方称新版应用加载速度提升超 50% ，并引入统一的跨应用入口，将静态提示框升级为任务感知系统。

**Original Link:**
https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/

### 技术与洞察

19. **Qwen 团队发布文生图评测基准 Qwen-Image-Bench**

**摘要:**
Qwen 团队推出文生图评测基准 Qwen-Image-Bench 及开源模型 Q-Judger 。官方称该基准含 56 个专业创作考点，其自动评分结果与人类专家评估高度相关。

**Original Link:**
https://github.com/QwenLM/Qwen-Image-Bench

20. **Sakana AI 提出 DiffusionBlocks 训练框架**

**摘要:**
Sakana AI 提出 DiffusionBlocks 训练框架，该框架将 Transformer 划分为多个独立块进行训练，且性能与端到端训练相当。代码已开源。

**Original Link:**
https://x.com/SakanaAILabs/status/2059648778051924281

21. **NVIDIA发布Dynamo Snapshot：K8s推理冷启动降至5秒内**

**摘要:**
NVIDIA 推出 Dynamo Snapshot ，结合 CRIU 与 cuda-checkpoint 技术，将 K8s 推理冷启动降至 5秒 内，目前该实验版仅限单 GPU 的 vLLM 与 SGLang 使用。

**Original Link:**
https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/

22. **小米分享 AI Coding 工程化实践：VAF、VKF 与 eight-claw**

**摘要:**
小米 发文分享了 小米 零售研发团队 AI Coding 工程化实践，通过构建统一工作流 VAF 、代码知识索引工具 VKF 及基于 飞书 的协作工作台 eight-claw ，解决 AI 提效仅局限于个体的问题，实现组织级提效与知识沉淀。

**Original Link:**
https://mp.weixin.qq.com/s/l5qeFWtXtaStweOqLP7RKA

### 行业动态

23. **豆包澄清“听信AI致婴儿喂养不足”传闻**

**摘要:**
豆包 回应婴儿喂养争议，指自媒体将“每顿”造谣为“每天”，且家长未提供完整对话背景。 豆包 同时强调 AI 内容仅供参考，不替代医嘱。

**Original Link:**
https://weibo.com/7778831349/R1vRkEqCY

24. **Linux Foundation 发布 OpenMDW-1.1，NVIDIA 宣布采用该模型许可证**

**摘要:**
Linux Foundation 发布专为 AI 模型打造的宽松许可证 OpenMDW ， NVIDIA 宣布在 Cosmos 、 Nemotron 等多个开源模型系列中采用该框架以简化许可。

**Original Link:**
https://openmdw.ai/


## Paper

1. **Towards Human-Like Interactive Speech Recognition With Agentic Correction and Semantic Evaluation**

**Publish Date:**
2026-05-29

**一句话总结:**
该论文提出 Agentic ASR 框架，将单次语音识别与语义纠错、意图路由和推理编辑结合，实现多轮交互式修正，并引入句子级语义错误率 S^2ER 及交互仿真系统，在多语言、命名实体密集和语码切换数据上验证了语义错误的显著降低。

**Link:**
https://arxiv.org/abs/2605.29430

2. **Notation Matters: A Benchmark Study of Token-Optimized Formats in Agentic AI Systems**

**Publish Date:**
2026-05-29

**一句话总结:**
该论文在四个智能体基准上评估了 TOON 和 TRON 两种令牌优化格式替代 JSON 的效果，发现 TRON 最多减少 27% 令牌且准确率接近基线，但 TOON 存在多轮解析失败与并行工具调用输出坍塌问题，为智能体系统中的工具调用格式选择提供了量化依据。

**Link:**
https://arxiv.org/abs/2605.29676

3. **CoHyDE: Iterative Co-Training of LLM Rewriter & Dense Encoder for Tool Retrieval**

**Publish Date:**
2026-05-29

**一句话总结:**
该论文提出 CoHyDE 方法，通过迭代联合训练稠密编码器与 LLM 重写器，使重写器生成目录风格描述并用偏好对齐优化，在 ToolBench 约 1 万工具子集上，尤其对模糊查询的检索 NDCG@5 提升高达 8 个百分点，证明了协同训练的关键作用。

**Link:**
https://arxiv.org/abs/2605.29271

4. **ParaTool: Shifting Tool Representations from Context to Parameters**

**Publish Date:**
2026-05-29

**一句话总结:**
ParaTool通过将每个工具封装为独立的参数模块，采用软选择门控聚合相关工具参数，并联合微调，实现无需上下文文档的工具调用，在Stable ToolBench与BFCL上显著超越上下文学习基线，降低推理开销，适用于高效智能体工具集成。

**Link:**
https://arxiv.org/abs/2605.29561

5. **ReasonOps: Operator Segmentation for LLM Reasoning Traces**

**Publish Date:**
2026-05-29

**一句话总结:**
ReasonOps通过无监督聚类将大模型思维链分解为回溯、推理等7种通用算子，在8个基准的4.4万条推理踪迹上验证了跨模型和领域的普遍性，并能早期预测答案正确性及识别模型身份，为优化推理策略提供了可操作分析工具。

**Link:**
https://arxiv.org/abs/2605.29192

6. **DenseSteer: Steering Small Language Models towards Dense Math Reasoning**

**Publish Date:**
2026-05-29

**一句话总结:**
DenseSteer提出一种训练无关的推理时引导框架，通过调制小型语言模型内部表示向密集推理模式偏移，在多个数学推理数据集上提升了小模型的准确率，且不增加负对数似然，适用于低资源场景下的数学问题求解。

**Link:**
https://arxiv.org/abs/2605.29247

7. **Rubric-Guided Process Reward for Stepwise Model Routing**

**Publish Date:**
2026-05-29

**一句话总结:**
为解决分步模型路由中过程奖励缺失，RoRo收集多样路由轨迹并基于结果、成本与过程质量构建偏好对，交替训练Rubricor与Judge生成步骤级评分，再结合GRPO优化策略，在五个推理基准上实现更好的准确率-成本权衡，适用于多模型协作推理场景。

**Link:**
https://arxiv.org/abs/2605.29310

8. **Surfacing Isolated Learners with Outcome-Independent Mediation of Feedback between Teachers and Students Using AI**

**Publish Date:**
2026-05-29

**一句话总结:**
设计一种不依赖成绩的透明排序机制，组合学习难点流行度、自陈差异和教师关注三个信号，在研究生课程中优先推荐主题，并发现该机制能识别单一信号无法捕获的孤立学习者（AUC 0.96），有助于人机共学。

**Link:**
https://arxiv.org/abs/2605.29240

9. **Adopt $\neq$ Adapt: Longitudinal Analyses of LLM Conversations in the Wild**

**Publish Date:**
2026-05-29

**一句话总结:**
分析约 1.2 万 Bing Copilot 用户和 WildChat-4.8M 的长期对话，发现个人层面行为几乎不变而群体趋势显著，活跃用户更成功且任务更专业，并指出 WildChat 偏向强力用户、不代表典型人机交互。

**Link:**
https://arxiv.org/abs/2605.29018

10. **When and How Human Curation Backfires: Preference Alignment under Multi-Model Self-Consuming Loop**

**Publish Date:**
2026-05-29

**一句话总结:**
形式化多模型自消费训练框架，研究人类策展在交互模型中的自影响与跨影响，证明当模型间存在交互时策展可能适得其反，导致长期偏好对齐倒退，扩展了此前单模型侧写的结论。

**Link:**
https://arxiv.org/abs/2605.29267
