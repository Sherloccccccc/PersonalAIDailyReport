# Daily AI Info

## News

### 模型发布

1. **蚂蚁百灵发布 Ring-2.6-1T，OpenRouter 免费试用一周**

**摘要:**
蚂蚁百灵团队 发布 万亿参数 旗舰思维模型 Ring-2.6-1T 。 该模型基于 63B 活跃参数，专为真实世界 Agent 工作流优化。 它具有自适应推理努力机制，在多项基准测试中成绩领先。 该模型目前已在 OpenRouter 和 Kilo Code 等平台开放 一周免费试用 。

**Original Link:**
https://x.com/AntLingAGI/status/2052808934390661134

2. **智谱发布 GLM-5V-Turbo 报告，开放Coding Plan用户申请使用**

**摘要:**
智谱AI 发布了 GLM-5V-Turbo 多模态基座模型的技术报告。 并向 GLM Coding Plan 用户开放该模型的体验申请。

**Original Link:**
https://zhipu-ai.feishu.cn/share/base/form/shrcndgpmRlJoD5rMmIavUrPwzg

3. **商汤科技推出SenseNova 6.7 Flash-Lite**

**摘要:**
商汤科技 推出轻量化多模态智能体模型 SenseNova 6.7 Flash-Lite 。 它取消视觉转文本中间层，能直接看懂复杂图表，实现感知到行动一体化。 用户可通过 办公小浣熊 免费体验该模型。

**Original Link:**
https://mp.weixin.qq.com/s/n5CZvuoHfjDsIPDmN0g6tA

4. **阶跃星辰发布 StepAudio 2.5 Realtime 实时语音大模型**

**摘要:**
阶跃星辰 推出端到端实时语音大模型 StepAudio 2.5 Realtime 。 该模型主打中英文“活人感”对话，能精准捕捉轻笑等副语言细节并动态调整回应。 该模型已在 Step Plan 等渠道全量上线。

**Original Link:**
https://stepaudiollm.github.io/step-audio-2.5-realtime/

5. **AI2 发布 EMO 模型，实现混合专家语义模块化**

**摘要:**
AI2 发布全新的端到端预训练混合专家模型 EMO 。 它打破 Token 独立路由的惯例，利用文档边界作弱监督。 促使 expert 按新闻、健康等语义领域自发形成模块，让模型能高效调用专家子集。

**Original Link:**
https://allenai.org/blog/emo

6. **千问团队开源 WebWorld 世界模型面向 Web Agent 训练**

**摘要:**
Qwen 团队开源了 WebWorld 大型开放网络世界模型系列。 该系列包含基于 Qwen3 微调的 8B 、 14B 和 32B 三个版本。 模型基于百万条真实网页轨迹训练，专供 Web Agent 的训练与评估使用。

**Original Link:**
https://github.com/QwenLM/WebWorld

### 开发生态

7. **OpenClaw 发布 2026.5.7 版，强化权限与更新流程**

**摘要:**
OpenClaw 发布 2026.5.7 版本。 新版本强化了原生命令与 Active Memory 权限管控。 同时优化了 CLI 工具及插件 npm 更新流程。

**Original Link:**
https://x.com/openclaw/status/2052508303687651717

8. **AWS 发布 Agent Toolkit for AWS 工具集**

**摘要:**
AWS 发布了 Agent Toolkit for AWS 工具集。 它整合 MCP 服务器、技能与插件，能辅助 Claude Code 等编程 Agent 在 AWS 上构建应用。

**Original Link:**
https://github.com/aws/agent-toolkit-for-aws

9. **Kiro 首次付费奖励 20 美元等值积分**

**摘要:**
Kiro 推出升级奖励。 通过社交登录或 Builder ID 首次升级至任意付费计划的用户，绑定信用卡后，可获得价值 20 美元 的 1000 积分额度。

**Original Link:**
https://kiro.dev/blog/new-paid-tier-bonus/

### 产品应用

10. **Grok 连接器功能正式上线安卓 iOS 及网页端**

**摘要:**
Grok 宣布连接器功能已在安卓、iOS及网页端上线，所有订阅用户均可使用。

**Original Link:**
https://x.com/grok/status/2052782088181727613

11. **Google Health Coach 结束预览面向全球上线**

**摘要:**
谷歌 宣布基于 Gemini 模型的 AI 健康教练 Google Health Coach 正式上线。 该服务率先面向 Fitbit 与 Pixel Watch 用户推出。 Google AI Pro 与 Ultra 用户可免费使用。

**Original Link:**
https://blog.google/products-and-platforms/products/google-health/google-health-coach/

### 技术与洞察

12. **Anthropic 发文阐述消除 Claude 的 agentic misalignment 行为**

**摘要:**
Anthropic 发布一项题为“Teaching Claude why”的研究，详细阐述了其如何消除 Claude 模型中的 agentic misalignment 行为。 研究发现，仅通过行为示范进行训练效果有限，而教导模型深刻理解伦理原则能带来更根本的改善。

**Original Link:**
https://www.anthropic.com/research/teaching-claude-why

13. **MiniMax 修复 M2 模型稀疏 Token 遗忘及小语种混杂问题**

**摘要:**
MiniMax 团队成员在知乎发布分析，解释 M2 系列模型无法生成 马嘉祺 等低频词的问题。 这源于后训练数据分布不均，导致低频 Token 在输出层发生表征漂移。 官方通过混入覆盖全词表的合成数据进行修复，成功解决了词汇遗忘问题，并将日语等小语种混淆率降至 百分之 1 。

**Original Link:**
https://mp.weixin.qq.com/s/jAvdxWaE6AvYqx_drcSjGA

14. **Google DeepMind 发布 AI Co-Mathematician**

**摘要:**
Google DeepMind 发布 AI Co-Mathematician 多 Agent 工作台，辅助数学家进行定理证明与理论构建，并在 FrontierMath Tier 4 测试中以 48% 的得分创下新高。 同时， Alex Imas 出任该部门 AGI 经济学总监，研究前沿 AI 对经济与工作形态的重塑。

**Original Link:**
https://x.com/pushmeet/status/2052812585804685322

15. **阿里巴巴提出 CDM 框架，四步推理实现图像生成最优**

**摘要:**
阿里巴巴 联合高校团队提出“连续时间分布匹配” CDM 框架，将扩散模型的蒸馏从离散锚点推向连续时间优化。 该方案仅需 4 步 推理即可实现 SOTA 级图像生成质量。

**Original Link:**
https://byliutao.github.io/cdm_page/

16. **Claude Code团队成员发文主张 HTML 替代 Markdown 作为 Agent 输出格式**

**摘要:**
Claude Code 团队成员发文，主张用 HTML 替代 Markdown 作为 Agent 输出格式。 HTML 能集成 CSS 和交互组件，大幅提升信息密度与双向交互体验。

**Original Link:**
https://x.com/trq212/status/2052809885763747935

17. **Nathan Lambert发文总结其中国AI实验室之行**

**摘要:**
AI2 成员 Nathan Lambert 发文总结其中国 AI 实验室之行。 他观察到，中国团队凭借年轻化与扁平化结构，形成了专注打磨 大语言模型 的工程文化。 这一生态展现出用较少资源构建前沿 模型 的独特优势。

**Original Link:**
https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs

### 行业动态

18. **DeepSeek 网页与 API 服务发生短时间大规模中断**

**摘要:**
DeepSeek 网页端与 API 服务于 5 月 8 日 下午发生约一个小时的大规模中断，系统频繁报出 429 、 503 等错误，并提示服务太忙。 当天下午 6 点 05 分 ，网页与 API 服务已全面恢复正常，官方暂未公布具体中断原因。

**Original Link:**
https://status.deepseek.com/

19. **Anthropic 一季度营收增 80 倍，Mythos 能力遭质疑**

**摘要:**
Anthropic CEO Amodei 透露， Anthropic 今年一季度营收与使用量暴增 80倍 。他还澄清 Mythos 模型供给难点在于控制访问权限以防范风险而非算力限制。 与此同时有相关讨论指出，旧模型也能发现 Mythos 模型发现的相同漏洞，质疑其能力涉嫌夸大炒作。

**Original Link:**
https://www.cnbc.com/2026/05/06/anthropic-ceo-dario-amodei-says-company-crew-80-fold-in-first-quarter.html

20. **Cloudflare 裁减 1100 人适应 AI Agent 时代重构组织**

**摘要:**
Cloudflare 宣布将全球裁减超过 1100 名员工。 此次调整旨在为 AI Agent 时代重构组织架构。 离职员工将获得包含支付至 2026 年底全额基本工资在内的丰厚补偿。

**Original Link:**
https://blog.cloudflare.com/building-for-the-future/

21. **NVIDIA 与 IREN 合作，将部署 5 吉瓦 AI 基础设施涉 21 亿美元投资**

**摘要:**
NVIDIA 与 IREN 宣布战略合作，计划结合 DSX AI 工厂架构与数据中心专长，部署高达 5 吉瓦的AI基础设施。 IREN 授予 NVIDIA 最高 21 亿美元的购股权。双方将重点在德克萨斯州园区开展部署。

**Original Link:**
https://nvidianews.nvidia.com/news/nvidia-and-iren-announce-strategic-partnership-to-accelerate-deployment-of-up-to-5-gigawatts-of-ai-infrastructure

22. **三部门印发智能体规范意见，明确 19 个典型应用场景**

**摘要:**
国家网信办 等部门印发《智能体规范应用与创新发展实施意见》。 文件明确 智能体 是具备自主感知与执行能力的系统，要求通过建立分类分级治理框架来守牢安全底线。

**Original Link:**
https://mp.weixin.qq.com/s/n-y34W_XZiV5lCKHOkok2g

### 前瞻与传闻

23. **DeepSeek 传筹备 500 亿融资，6 月发布 V4.1 模型**

**摘要:**
据报道， DeepSeek 正筹备目标达 500亿元 人民币的首轮外部融资。 完成后估值有望突破 3500亿元 。 报道还指出，为加速商业化，该公司计划于 6月 推出具备处理图像与音频能力的 V4.1 模型。 相关融资与产品信息仍有待官方证实。

**Original Link:**
https://www.theinformation.com/articles/deepseek-to-raise-more-than-7-billion-as-startup-plots-revenue-efforts

24. **阶跃星辰传完成 25 亿美元融资，加速筹备赴港上市**

**摘要:**
据报道， 阶跃星辰 即将完成近 25亿美元 融资，有望成为中国大模型领域最大单笔融资。 报道指出， 阶跃星辰 已拆除红筹架构并完成股改，加速筹备赴港上市。

**Original Link:**
https://zhidx.com/p/556043.html


## Paper

1. **Why Global LLM Leaderboards Are Misleading: Small Portfolios for Heterogeneous Supervised ML**

**Publish Date:**
2026-05-07

**一句话总结:**
该论文分析Arena平台52个模型在116种语言上的8.9万次比较，揭示全局排名因语言任务异质性而误导，提出(λ,ν)-组合框架，用5个局部排名覆盖96%投票，并应用于模型选择与公平性分类。

**Link:**
https://arxiv.org/abs/2605.06656

2. **Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients**

**Publish Date:**
2026-05-07

**一句话总结:**
该论文提出仅用正向样本的强化学习框架POPO，通过有界重要性采样和概率重分配实现隐式负梯度，利用孪生动量网络稳定优化，在Qwen-Math-7B上AIME 2025达36.67%，超越GRPO的30%。

**Link:**
https://arxiv.org/abs/2605.06650

3. **PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization**

**Publish Date:**
2026-05-07

**一句话总结:**
提出PairAlign框架，将音频标记化作为条件序列生成任务，通过跨视图自对齐学习紧凑、有序的符号序列，在3秒语音上实现强跨视图一致性和广泛词表使用，并在TIMIT检索中减少55%标记量且保持编辑距离搜索。

**Link:**
https://arxiv.org/abs/2605.06582

4. **When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels**

**Publish Date:**
2026-05-07

**一句话总结:**
该论文提出无基准条件下的LLM安全对比评分框架，通过工具有效性链（安全与擦除模型对比、方差分析、重运行稳定性）验证审计，在挪威语安全包上达到AUROC 0.89-1.00，并用于公共部门采购模型比较。

**Link:**
https://arxiv.org/abs/2605.06652

5. **UniSD: Towards a Unified Self-Distillation Framework for Large Language Models**

**Publish Date:**
2026-05-07

**一句话总结:**
UniSD提出统一的LLM自蒸馏框架，整合多教师一致性、EMA教师稳定、token级对比学习、特征匹配和散度裁剪，系统研究各组件作用，在六项基准上平均提升5.4分，证明自蒸馏无需外部教师即可高效适配LLM。

**Link:**
https://arxiv.org/abs/2605.06597

6. **Directional Consistency as a Complementary Optimization Signal: The GONO Framework**

**Publish Date:**
2026-05-07

**一句话总结:**
GONO优化器通过梯度方向一致性动态调整Adam动量系数，利用方向对齐与损失下降解耦现象区分停滞区与收敛，在MNIST、CIFAR-10和ResNet-18上取得竞争精度，代码开源。

**Link:**
https://arxiv.org/abs/2605.06575

7. **SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders**

**Publish Date:**
2026-05-07

**一句话总结:**
本文提出SoftSAE稀疏自编码器，通过可微Soft Top-K机制让模型根据输入复杂度自适应选择激活特征数量，解决了固定Top-K稀疏度无法匹配数据局部内在维度变化的问题，在LLM和ViT的可解释性实验中能更准确地提取合适数量的可解释特征。

**Link:**
https://arxiv.org/abs/2605.06610

8. **FedAttr: Towards Privacy-preserving Client-Level Attribution in Federated LLM Fine-tuning**

**Publish Date:**
2026-05-07

**一句话总结:**
FedAttr 提出一种联邦学习中客户级归属协议，通过成对子集差分估计、水印检测评分及 Stouffer 方法组合，在保护安全聚合隐私的同时精准识别使用水印数据训练的客户，经验证达到 100% 真阳性和 0% 假阳性，且仅增加 6.3% 额外开销。

**Link:**
https://arxiv.org/abs/2605.06596

9. **Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models**

**Publish Date:**
2026-05-07

**一句话总结:**
本文立场鲜明地论证基础模型的分布外泛化必需引入代理范式，通过阶段感知形式化、参数覆盖天花板证明及定义代理的四项结构特性，说明代理系统可扩展纯模型中心方法的可达集，并提出互补研究议程，推动代理成为独立研究方向。

**Link:**
https://arxiv.org/abs/2605.06522

10. **Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning**

**Publish Date:**
2026-05-07

**一句话总结:**
该工作提出协调感知的协作多智能体强化学习评估视角和STAT测试平台，通过承诺约束任务分配实验揭示回报趋势相似的背后存在不同协调机制，如冗余分配和任务完成效率差异。

**Link:**
https://arxiv.org/abs/2605.06557
