# Daily AI Info

## News

### 模型发布

1. **百度宣布文心 5.1 模型正式上线**

**摘要:**
百度 宣布 文心 5.1 大模型正式上线，用户可登录官网或 星河社区 Playground 体验。该模型总参数较前代压缩至 三分之一 ，预训练成本仅为同规模 百分之六 。现正陆续上架 数十 个创作 Agent 平台。

**Original Link:**
https://yiyan.baidu.com/blog/zh/posts/ernie-5.1-0508-release/

2. **HiDream-ai 开源 HiDream-O1-Image 图像生成模型**

**摘要:**
HiDream-ai 团队开源了 8B 参数的图像生成模型 HiDream-O1-Image 。该模型基于统一 Transformer 架构，无需外部 VAE 即可原生生成 2048 分辨率图像。

**Original Link:**
https://github.com/HiDream-ai/HiDream-O1-Image

### 开发生态

3. **OpenRouter 推出 Pareto Code 实验性编码路由**

**摘要:**
OpenRouter 推出了实验性编码路由 Pareto Code 。该路由会根据 ArtificialAnalysis 排名，自动把任务分配给满足分数要求且成本最低的模型，并提供了提速的 Nitro 版本。

**Original Link:**
https://x.com/OpenRouter/status/2053170520087024109

### 技术与洞察

4. **OpenAI 公开内部 Codex 安全运行实践**

**摘要:**
OpenAI 近期分享了一篇关于其如何在内部安全运行 Codex 的技术实践文章，重点介绍了沙箱执行边界、审批策略、自动审核模式、网络策略、身份验证绑定、命令规则以及 Agent 原生遥测等控制措施。

**Original Link:**
https://openai.com/index/running-codex-safely/

5. **Perplexity 公开内部 Agent Skills 设计维护指南**

**摘要:**
Perplexity 发文介绍其内部 Agent Skills 的设计与维护指南。其指出：构建 Skill 需先编写评估，抓住描述中的触发词，用层级组织复杂知识，再通过记录失败案例的 gotchas 飞轮持续维护。

**Original Link:**
https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity

### 行业动态

6. **Nous Research 宣布 Hermes Agent 登顶 OpenRouter 应用用量榜**

**摘要:**
Nous Research 团队宣布，旗下 Hermes Agent 在 OpenRouter 平台全球 Token 排名中超越 OpenClaw 登顶，拿下所有 AI 应用第一名。

**Original Link:**
https://x.com/NousResearch/status/2052904761087729897

7. **消息称 Anthropic 与 Akamai 签署 18 亿美元七年合同**

**摘要:**
据报道， Anthropic 与云服务商 Akamai 签署了价值 十八亿美元 、为期 七年 的 云基础设施 服务合同，以满足其日益增长的算力需求。受此大单提振， Akamai 股价连续大涨。

**Original Link:**
https://www.globenewswire.com/news-release/2026/05/07/3290507/0/en/akamai-reports-first-quarter-2026-financial-results.html

### 前瞻与传闻

8. **报道称字节跳动今年 AI 基建支出超两千亿**

**摘要:**
据报道， 字节跳动 今年 AI 基础设施支出将超 2000亿元 ，较原计划至少增加 25% ，更多预算投向国产 AI 芯片。

**Original Link:**
https://www.scmp.com/tech/article/3352736/tiktok-makes-record-us25b-investment-expand-digital-infrastructure-thailand


## Paper

1. **Market-Alignment Risk in Pricing Agents: Trace Diagnostics and Trace-Prior RL under Hidden Competitor State**

**Publish Date:**
2026-05-07

**一句话总结:**
该论文在双酒店收益管理模拟器中，发现标准RL定价智能体因部分可观测和奖励错位导致市场行为崩溃，提出基于历史市场痕迹的分布先验和KL惩罚的Trace-Prior RL方法，使智能体在优化自身收益的同时匹配市场价格分布，并提供完整的痕迹诊断工具集。

**Link:**
https://arxiv.org/abs/2605.06529

2. **SNAPO: Smooth Neural Adjoint Policy Optimization for Optimal Control via Differentiable Simulation**

**Publish Date:**
2026-05-07

**一句话总结:**
SNAPO框架将神经网络策略与可微仿真器结合，用平滑逼近替代硬约束，通过一次伴随传递计算所有策略参数和目标函数的精确梯度，在天然气存储、养老金资产管理和制药反应链控制中实现了秒级训练和毫秒级敏感度计算。

**Link:**
https://arxiv.org/abs/2605.06570

3. **Recursive Agent Optimization**

**Publish Date:**
2026-05-07

**一句话总结:**
递归代理优化（RAO）用强化学习训练代理递归生成和委托子任务，实现分治式推理扩展，可处理超上下文窗口任务并泛化至更难问题，同时减少训练和推理用时。

**Link:**
https://arxiv.org/abs/2605.06639

4. **Crafting Reversible SFT Behaviors in Large Language Models**

**Publish Date:**
2026-05-07

**一句话总结:**
提出通过联合优化路由掩码和模型权重将SFT诱导的行为压缩为稀疏、因果必要的子网络，并利用激活匹配优化的软提示在推理时实现行为逆转，在安全与风格任务上验证了可控性，为部署模型的实时行为管理提供新方案。

**Link:**
https://arxiv.org/abs/2605.06632

5. **Is One Layer Enough? Understanding Inference Dynamics in Tabular Foundation Models**

**Publish Date:**
2026-05-07

**一句话总结:**
论文首次系统分析六种表格基础模型的每层推理动态，发现深度冗余，设计循环单层模型仅用20%参数达到可比性能，并开源代码，有望简化表格AI产品的部署。

**Link:**
https://arxiv.org/abs/2605.06510

6. **MARBLE: Multi-Aspect Reward Balance for Diffusion RL**

**Publish Date:**
2026-05-07

**一句话总结:**
MARBLE在扩散模型强化学习中，为每个奖励保持独立优势估计，通过二次规划在梯度空间平衡多奖励更新方向，消除手动加权，在SD3.5上同时提升五项奖励指标，且训练速度接近单奖励基线。

**Link:**
https://arxiv.org/abs/2605.06507

7. **Verifier-Backed Hard Problem Generation for Mathematical Reasoning**

**Publish Date:**
2026-05-07

**一句话总结:**
VHG框架通过引入独立验证器到设置者-求解者对弈中，让设置者奖励由问题有效性和难度联合决定，使用硬符号或软LLM验证器，在不定积分和通用数学推理任务上生成的问题难度和有效性显著优于基线。

**Link:**
https://arxiv.org/abs/2605.06660

8. **Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key**

**Publish Date:**
2026-05-07

**一句话总结:**
通过构建可独立控制推理深度和逻辑表达力的合成框架ScaleLogic，该研究发现强化学习训练计算量随深度呈幂律增长，且更高表达力的逻辑训练能更高效地迁移至数学和通用推理基准，指导更经济的推理模型训练。

**Link:**
https://arxiv.org/abs/2605.06638

9. **Cross-Modal Navigation with Multi-Agent Reinforcement Learning**

**Publish Date:**
2026-05-07

**一句话总结:**
CRONA框架通过多智能体强化学习实现视觉-声学跨模态导航，利用辅助信念和集中式多模态评论家增强协作，实验表明轻量级代理协作在短距离和大规模环境中均比单体模型更高效、更灵活。

**Link:**
https://arxiv.org/abs/2605.06595

10. **DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency**

**Publish Date:**
2026-05-07

**一句话总结:**
DINORANKCLIP提出高阶Plackett-Luce排序一致损失和冻结DINOv3教师蒸馏的多尺度融合模块，在Conceptual Captions 3M上训练，显著提升CLIP在细粒度和分布外评测上的局部结构推理性能。

**Link:**
https://arxiv.org/abs/2605.06592
