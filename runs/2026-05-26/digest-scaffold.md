# Daily AI Info

## News

### 模型发布

1. **SpaceXAI 完成 Grok V9-Medium 模型训练并预告开源计划**

**摘要:**
Elon Musk 宣布， 1.5T 参数的 Grok 基础模型 V9-Medium 已完成训练并进入微调阶段，几天后启动强化学习，预计在 2 到 3 周 内公开发布，同时他还回应网友评论称，将在 今年年底 开源 0.5T 参数的模型。

**Original Link:**
https://x.com/elonmusk/status/2058787384364265734

2. **OpenBMB 发布 MiniCPM5-1B 开源模型**

**摘要:**
OpenBMB 开源了 MiniCPM5-1B 模型。该模型具备混合推理能力，登顶了 Artificial Analysis 小模型榜单，成为 2B 以下最强模型。

**Original Link:**
https://huggingface.co/openbmb/MiniCPM5-1B

### 开发生态

3. **Grok Build 面向 SuperGrok 和 X Premium+ 用户开放**

**摘要:**
SpaceXAI 宣布 Grok Build 现已开启 Beta 测试，并面向所有 SuperGrok 和 X Premium+ 用户开放，支持 Plan Mode 、 Imagine 媒体生成及通过 CLI 构建自动化任务。

**Original Link:**
https://x.com/xai/status/2058973760708091907

4. **Google Antigravity 新增 Gemini 3.5 Flash (Low)**

**摘要:**
Antigravity 宣布引入 Gemini 3.5 Flash (Low) 选项，官方称其生成 token 数较 Medium 版减少约 45% 以优化简单任务，同时已重置所有付费用户的配额。

**Original Link:**
https://x.com/antigravity/status/2058741814237241812

### 产品应用

5. **ima 宣布全面开放 copilot 并上线 Skill 发布功能**

**摘要:**
ima 宣布取消排队限制，全面开放具备记忆与知识库的 Agent “copilot” ，同时知识号同步上线发布 Skill 功能，用户需将应用更新至最新版即可体验。

**Original Link:**
https://mp.weixin.qq.com/s/R22ySmNraCJ4W4o2nbJu1w

### 技术与洞察

6. **华为发布韬(τ)定律：麒麟芯片将首发逻辑折叠技术**

**摘要:**
华为 近日提出半导体发展新原则—— 韬定律 。该定律主张以“时间缩微”替代传统的“几何缩微”，通过“逻辑折叠”等创新技术压缩信号传播时延，从而持续提升晶体管密度与系统性能。

**Original Link:**
https://mp.weixin.qq.com/s/txF-C8pXnmGwqNLFEDep8A

### 前瞻与传闻

7. **社区反馈 Claude 注册疑似取消手机验证并重开申诉**

**摘要:**
据 社区 用户反馈，近期 Claude 账号注册疑似取消了手机号验证，同时还开放了此前被封禁账号的申诉入口。

**Original Link:**
https://linux.do/t/topic/2245547


## Paper

1. **What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA**

**Publish Date:**
2026-05-25

**一句话总结:**
本文发现医学 RAG 中检查器的输出分布而非准确度决定训练梯度，揭示信号崩溃和奖励黑客现象，并指出使用适度信号的本地分类器可训练出比强信号模型质量更高的问答代理，结果为验证器即奖励系统提供了边界条件。

**Link:**
https://arxiv.org/abs/2605.25988

2. **QUIET: A Multi-Blank Cascaded Story Cloze Benchmark for LLM Creative Generation Capability**

**Publish Date:**
2026-05-25

**一句话总结:**
本文提出 QUIET 基准，在结构化故事中设置 10-20 个具有级联依赖的空白，让模型开放式填空，并通过基于约束满足与信息惊喜的自动评分协议来客观评估大语言模型的创造性生成能力。

**Link:**
https://arxiv.org/abs/2605.25955

3. **Beyond Summaries: Structure-Aware Labeling of Code Changes with Large Language Models**

**Publish Date:**
2026-05-25

**一句话总结:**
本文提出了一种两阶段流水线，利用大语言模型对代码变更进行结构化标记，通过少量提示生成语言无关的标签，在手动标注的基准上达到了 84% 召回率和 81% 精确率，可用于增强代码审查自动化。

**Link:**
https://arxiv.org/abs/2605.26100

4. **Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning**

**Publish Date:**
2026-05-25

**一句话总结:**
该研究提出正交瓶颈方法，通过固定的正交投影将强化学习的编码器特征约束到低维子空间，在不改变RL算法的情况下保持价值函数表达性，实验表明在性能和表示几何上具有优势，为RL的流形假设提供了表征空间解释。

**Link:**
https://arxiv.org/abs/2605.26012

5. **StakeBench: Evaluating Language Understanding Grounded in Market Commitment**

**Publish Date:**
2026-05-25

**一句话总结:**
该研究提出StakeBench评估框架，基于Polymarket和Manifold的56万条评论及交易记录，以市场行为监督取代人工标注，测试LLM检测市场承诺、识别立场、预测行动和赔率投影能力，发现多数模型存在结构缺陷，为金融NLP提供行为锚定基准。

**Link:**
https://arxiv.org/abs/2605.26074

6. **Step-TP: A Grounded, Step-Level Dataset with Chain-of-Thought Reasoning for LLM-Guided Tensor Program Optimization**

**Publish Date:**
2026-05-25

**一句话总结:**
该论文提出Step-TP数据集，为LLM引导的张量程序优化提供原子化步骤级监督和结构化思维链，采用可验证的中间表示和组合优化策略，旨在增强LLM在大型组合优化空间中的单步决策可靠性，适用于编译器自动化优化。

**Link:**
https://arxiv.org/abs/2605.25954

7. **MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research**

**Publish Date:**
2026-05-25

**一句话总结:**
这篇论文提出一个可复用框架，面向大模型能力评测；用途是给模型、agent 或工具链提供更可复现的横向比较标准。

**Link:**
https://arxiv.org/abs/2605.26114

8. **From Model Scaling to System Scaling: Scaling the Harness in Agentic AI**

**Publish Date:**
2026-05-25

**一句话总结:**
这篇论文构建一个新的 benchmark，面向检索增强生成或复杂信息检索任务；通过实验或基准测试验证方法是否真的改善任务表现；用途是判断检索系统能否为复杂推理持续提供有效证据。

**Link:**
https://arxiv.org/abs/2605.26112

9. **LLM-driven design of physics-constrained constitutive models: two agents are better than one**

**Publish Date:**
2026-05-22

**一句话总结:**
本文提出多智能体LLM方法，由Creator生成本构模型、Inspector逐项审计物理约束，将Claude Opus生成模型的约束满足率从91%提升至100%，在脑组织与橡胶数据上保持高精度和良好外推，实现可信自动化本构建模。

**Link:**
https://arxiv.org/abs/2605.23754

10. **BoostTaxo: Zero-Shot Taxonomy Induction via Boosting-Style Agentic Reasoning and Constraint-Aware Calibration**

**Publish Date:**
2026-05-15

**一句话总结:**
BoostTaxo利用粗细结合的LLM增强式推理与结构感知校准，在零样本条件下从领域术语自动构建语义层级，在三个公开数据集上性能领先，消融实验验证了混合候选选择与分数校准的有效性。

**Link:**
https://arxiv.org/abs/2605.12520
