# Daily AI Info

## News

### 模型发布

1. **Cohere 发布其首个编程模型 BLS-Mini-Code-1.0 早期权重**

**摘要:**
Cohere 团队在 Hugging Face 上发布了其首个编程模型 BLS-Mini-Code-1.0 的早期访问版本，该模型总参数量为 30B 、活跃参数量为 3B ，目前正面向社区开放测试以收集反馈。

**Original Link:**
https://huggingface.co/CohereLabs/BLS-Mini-Code-1.0

2. **研究团队推出开源 20B 搜索 Agent Harness-1**

**摘要:**
UIUC 等大学联合团队发布并开源了名为 Harness-1 的 20B 参数搜索 Agent ，该模型通过在有状态搜索框架内进行强化学习训练，将检索状态外部化维护。

**Original Link:**
https://huggingface.co/pat-jj/harness-1

### 开发生态

3. **Nous Research 发布 Hermes Agent v0.16.0**

**摘要:**
Nous Research 正式发布 Hermes Agent v0.16.0 版本。该版本新增 原生桌面应用 并为其引入了简体中文支持，还将 Web Dashboard 升级为包含 MCP 管理的完整控制面板。

**Original Link:**
https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5

### 前瞻与传闻

4. **消息称OpenAI与美政府正谈判入股事宜**

**摘要:**
据报道， OpenAI 正与美国政府探讨入股事宜，拟通过捐赠股份设立向公众分红的公共财富基金。由于法律机制尚不明确，该谈判仍有流产可能。

**Original Link:**
https://the-decoder.com/openai-and-the-trump-administration-are-negotiating-a-government-stake-in-the-ai-startup/

5. **消息称 Anthropic 新模型 Claude Mythos 5 在 API 中短暂现身**

**摘要:**
据社区成员爆料，名为 Claude Mythos 5 的未发布模型在 Anthropic 的 API 及开发者模式中短暂现身。此现象引发了关于该模型即将发布的猜测，但官方尚未发表任何回应。

**Original Link:**
https://x.com/testingcatalog/status/2063234385227252184


## Paper

1. **In-Context Multiple Instance Learning**

**Publish Date:**
2026-06-04

**一句话总结:**
本文提出上下文多实例学习，用合成数据预训练感知器架构模型，在新任务上仅需少量标注包即可单次前向分类，在十二个基准上超越任务特定训练的有监督基线。

**Link:**
https://arxiv.org/abs/2606.06458

2. **CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments**

**Publish Date:**
2026-06-04

**一句话总结:**
CollabSim是一个基于CSCW理论的多智能体协作能力评估框架，通过可控仿真实验记录行动级内部状态，在四个大语言模型上量化代理的共同基础建立和意图理解能力，揭示了任务结构对协作的影响，为设计协作型AI代理提供了评估基准。

**Link:**
https://arxiv.org/abs/2606.06399

3. **Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration**

**Publish Date:**
2026-06-04

**一句话总结:**
ALMANAC是一个基于地图任务的人类协作数据集，包含2987个行动级协作动作，每个动作均标注了参与者自我推理、对伙伴意图感知和团队目标的心智模型，并在六个大语言模型上评测了预测行为和心智模型的能力，为开发具备协作心智建模能力的AI代理提供了数据支撑。

**Link:**
https://arxiv.org/abs/2606.06388

4. **From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws**

**Publish Date:**
2026-06-04

**一句话总结:**
该论文提出HarnessFix框架，通过构建Harness-aware Trace IR并基于轨迹证据归因故障到具体步骤和层，生成并验证补丁，在SWE-Bench Verified等四个基准上提升性能15.2%-50.0%，显著改善LLM智能体的可靠性。

**Link:**
https://arxiv.org/abs/2606.06324

5. **Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution**

**Publish Date:**
2026-06-04

**一句话总结:**
Code2LoRA利用超网络为代码大模型生成仓库特定的LoRA适配器，支持静态和动态代码演进场景，在RepoPeftBench基准上实现63.8%和60.3%的准确率，无需额外推理开销。

**Link:**
https://arxiv.org/abs/2606.06492

6. **HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers**

**Publish Date:**
2026-06-04

**一句话总结:**
HANDOFF提出一种人形机器人全身控制器，通过多教师KL蒸馏将运动跟踪、移动和跌倒恢复三个专家模型融合为混合专家学生，在Unitree G1上实现领先的速度跟踪和大范围操作空间，并由VLM驱动的代理规划器完成自然语言任务。

**Link:**
https://arxiv.org/abs/2606.06493

7. **USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding**

**Publish Date:**
2026-06-04

**一句话总结:**
USAD 2.0通过领域感知蒸馏和监督蒸馏整合自监督与监督基础模型，构建了覆盖语音、音乐等多领域的通用音频编码器，缩放至十亿参数后在探测任务和LLM评估中取得最佳效果。

**Link:**
https://arxiv.org/abs/2606.06444

8. **Latent Reasoning with Normalizing Flows**

**Publish Date:**
2026-06-04

**一句话总结:**
提出NF-CoT，在LLM内部嵌入标准化流建模紧凑连续思维，实现保留自回归解码和KV缓存的潜在推理，在代码生成上提升通过率并降低中间推理成本。

**Link:**
https://arxiv.org/abs/2606.06447

9. **Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation**

**Publish Date:**
2026-06-05

**一句话总结:**
该论文首次系统评估 LLM 从自然语言生成 TLA+ 规范的能力，在 205 个规范上测试 30 个模型，仅 8.6% 最高语义正确率，模型大小不预示质量，代码专长模型因负迁移表现更差，识别五类幻觉并发布评估框架。

**Link:**
https://arxiv.org/abs/2606.05792

10. **BBOmix: A Tabular Benchmark for Hyperparameter Optimization of Unsupervised Biological Representation Learning**

**Publish Date:**
2026-06-03

**一句话总结:**
BBOmix 是首个面向无监督生物表示学习的表格基准，涵盖 105,000 次评估、四种自编码器架构和七种多组学模态，量化了重建损失与下游性能相关性，并提供多种 HPO 方法的基线，旨在使大规模无监督超参优化研究更易于访问和复现。

**Link:**
https://arxiv.org/abs/2606.05139
