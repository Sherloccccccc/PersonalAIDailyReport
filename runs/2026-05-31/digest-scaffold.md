# Daily AI Info

## News

### 模型发布

1. **阶跃星辰为 Hermes Agent 用户提供 Step 3.7 Flash 模型限时免费服务**

**摘要:**
阶跃星辰的新模型 Step 3.7 Flash 目前正通过 Nous Portal ，面向 Hermes Agent 用户开展为期 30 天 的免费开放活动。

**Original Link:**
https://x.com/StepFun_ai/status/2060726184712052849

### 开发生态

2. **OpenClaw 发布 2026.5.28 版本**

**摘要:**
OpenClaw 发布 2026.5.28 版本，新增支持 Claude Opus 4.8 模型及通过 fal 接入的 Krea 图像模型，官方称该版本冷启动快 14.5% 、热启动快 16.0% 、新安装体积缩小 52.8% 。

**Original Link:**
https://x.com/openclaw/status/2060843306100183541

### 技术与洞察

3. **小米详解 MiMo-V2.5 推理优化**

**摘要:**
小米MIMO团队 发布了 MiMo-V2.5 系列模型推理优化技术报告，通过重构 KVCache 系统和引入自研分布式缓存 GCache ，官方称成功兑现了 Hybrid SWA 架构的效率潜力，使线上服务端 KV Cache 命中率平均达 93% ，并将由此节省的成本通过 API 降价回馈用户。

**Original Link:**
https://mp.weixin.qq.com/s/3e8ms4m00NbRVicLry1oAQ

### 行业动态

4. **MiniMax 启动 A 股 IPO 进程**

**摘要:**
据媒体报道， MiniMax 已于 5 月 29 日 同 中信证券 签署辅导协议，正式启动 A 股 IPO 进程，此前该公司已于今年 1 月 在 港交所 上市。

**Original Link:**
https://zhidx.com/p/561711.html

5. **软银宣布在法国投资最高 750 亿欧元建设 AI 数据中心**

**摘要:**
软银 宣布计划在 法国 投资最高 750 亿欧元 ，开发并运营总容量 5 GW 的 AI 数据中心 ，其中第一阶段将投入 450 亿欧元 建设 3.1 GW 产能。

**Original Link:**
https://group.softbank/en/news/press/20260531_0

### 前瞻与传闻

6. **爆料称 ChatGPT 正在开发 "Translation Block"**

**摘要:**
据爆料博主称， OpenAI 正在为 ChatGPT 开发 "Translation Block" 翻译组件，其支持的语言中罕见地包含了《权力的游戏》虚构语言 "High Valyrian" 。

**Original Link:**
https://x.com/btibor91/status/2060811897495294445


## Paper

1. **Unlocking the Working Memory of Large Language Models for Latent Reasoning**

**Publish Date:**
2026-05-28

**一句话总结:**
该文提出名为RiM的潜在推理方法，用固定的记忆块序列替代中间推理词的自回归生成，通过两阶段课程训练，使大模型在单次前向传播中实现高效推理，性能匹配甚至超越现有方法。

**Link:**
https://arxiv.org/abs/2605.30343

2. **In-Context Reward Adaptation for Robust Preference Modeling**

**Publish Date:**
2026-05-28

**一句话总结:**
该论文提出In-Context Reward Adaptation框架，利用Transformer的上下文学习能力从少量偏好示例中在线推断奖励结构，并通过引入人类响应时间作为辅助信号克服渐进偏差，实现稳健的未见偏好建模；实验显示该方法能缓解分布偏移脆弱性，为灵活AI对齐提供扩展路径。

**Link:**
https://arxiv.org/abs/2605.30323

3. **Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection**

**Publish Date:**
2026-05-28

**一句话总结:**
Loong是一个长文档翻译智能体，通过3E记忆模块存储摘要、范例和实体，并利用强化学习从自身采样轨迹中学习自适应选择最优上下文，在英中德法等翻译方向上平均提升13.0分，且对超长文档和领域迁移鲁棒。

**Link:**
https://arxiv.org/abs/2605.30274

4. **Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents**

**Publish Date:**
2026-05-28

**一句话总结:**
该论文针对多组件LLM智能体中各组件局部一致但全局不一致问题，通过组合残差ε*的L2距离量化不一致程度，利用层次Boyle-Dykstra投影确定性修复组合，并提供随时有效的e-过程进行序贯监控；实验在多个模型集成团上检测到高比例不一致，证明了方法的必要性。

**Link:**
https://arxiv.org/abs/2605.30335

5. **When Should Models Change Their Minds? Contextual Belief Management in Large Language Models**

**Publish Date:**
2026-05-28

**一句话总结:**
本文针对大模型在持续交互中何时更新、维持或忽略信念的问题，提出上下文信念管理框架与BeliefTrack基准，通过强化学习训练显著降低信念管理失败率，并揭示表征层面的潜在动态。

**Link:**
https://arxiv.org/abs/2605.30219

6. **MarginGate: Sparse Margin-Triggered Verification for Batch-Invariant LLM Inference**

**Publish Date:**
2026-05-28

**一句话总结:**
该文提出MarginGate，利用logit边界值触发稀疏验证，在保持大模型批量推理确定性结果的同时，将验证触发率控制在18.56%至49.50%，显著降低了全量验证的延迟开销。

**Link:**
https://arxiv.org/abs/2605.30218

7. **CommunityFact: A Dynamic, Multilingual, Multi-domain Benchmark for Misinformation Detection in the Wild**

**Publish Date:**
2026-05-28

**一句话总结:**
本文提出CommunityFact动态多语言多域虚假信息检测基准，包含1.6万条声明，评估10种LLM在有/无网络搜索下的表现，发现网络访问显著改善核实效果但来源选择与社区笔记存在偏差，进而提出利用社区笔记训练来源建议器以改进事实核查。

**Link:**
https://arxiv.org/abs/2605.30241

8. **Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching**

**Publish Date:**
2026-05-28

**一句话总结:**
HullFT 采用凸重建将查询嵌入表示为少数训练样本的稀疏组合并进行整数化，利用梯度复用加速重复样本的微调，实验表明在更短总运行时间内获得更低的 bits-per-byte。

**Link:**
https://arxiv.org/abs/2605.30337

9. **DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation**

**Publish Date:**
2026-05-28

**一句话总结:**
DynaFLIP提出动力学感知的多模态预训练框架，通过图像-语言-3D流三元组最小化超球面单纯形体体积，使视觉编码器关注控制相关区域，在多种机器人操作任务中提升分布外泛化达22.5%。

**Link:**
https://arxiv.org/abs/2605.30350

10. **FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation**

**Publish Date:**
2026-05-26

**一句话总结:**
FoundObj提出一种无标注3D对象分割框架，基于超点的发现代理通过强化学习逐步合并邻近超点，利用自监督2D/3D基础模型的语义和几何奖励引导，在多个基准上超越现有方法，并展示零样本和长尾强泛化能力。

**Link:**
https://arxiv.org/abs/2605.27178
