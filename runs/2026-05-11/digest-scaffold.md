# Daily AI Info

## News

### 开发生态

1. **Codex 周安装量达 8610 万，12 倍于 Claude Code**

**摘要:**
据 a16z 引用 TickerTrends 的数据显示， Codex 的周安装量飙升至 8610 万 ，是 Claude Code 720 万 周安装量的 12 倍，该增长主要发生在 4 月底至 5 月初 。

**Original Link:**
https://www.a16z.news/p/charts-of-the-week-it-was-a-good

2. **Hermes Agent 新增 LINE 网关通道**

**摘要:**
Hermes Agent 宣布新增 LINE 作为官方支持的交互渠道，用户现可通过该平台与 Agent 进行互动。

**Original Link:**
https://hermes-agent.nousresearch.com/docs/user-guide/messaging/line

3. **OpenAI终止开发者自助微调通道**

**摘要:**
OpenAI 通过官方邮件宣布，将全面关停面向开发者的自助微调 API ，即日起新用户无法创建微调任务，现有用户可使用至 2027 年 1 月 6 日 ，已部署的微调模型推理服务将与底层基座模型生命周期绑定。

**Original Link:**
https://startupfortune.com/openai-is-winding-down-fine-tuning-and-that-changes-the-startup-playbook/

4. **Hugging Face 推出 hf-sandbox，基于 Jobs 打造云端代码沙箱**

**摘要:**
Hugging Face 发布了 hf-sandbox ，这是一个基于其 Jobs 服务构建的 Modal 风格沙箱 API，允许用户在云端安全地运行临时代码，目前已在 GitHub 开源。

**Original Link:**
https://github.com/huggingface/hf-sandbox

### 技术与洞察

5. **调查曝光“中转站”利用被盗凭证和模型替换盈利，并出售用户数据**

**摘要:**
据报道，一项调查发现被称为“ 中转站 ”的服务通过利用被盗凭证、替换 模型 及记录用户输入输出数据转售为训练数据等手段维持极低定价。

**Original Link:**
https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data

### 前瞻与传闻

6. **Jarred Sumner 透露正在将 Bun 运行时从 Zig 重写为 Rust**

**摘要:**
Bun 创始人 Jarred Sumner 透露其正在将 Bun 运行时从 Zig 重写为 Rust ，目前已完成约 96 万行代码的迁移。

**Original Link:**
https://x.com/jarredsumner/status/2053063524826620129


## Paper

1. **CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation**

**Publish Date:**
2026-05-08

**一句话总结:**
CA-SQL根据任务难度动态调整探索广度，结合进化提示和投票机制，在BIRD挑战子集上以GPT-4o-mini实现最佳性能。

**Link:**
https://arxiv.org/abs/2605.08057

2. **Collaborator or Assistnat? How AI Coding Agents Partition Work Across Pull Request Lifecycles**

**Publish Date:**
2026-05-08

**一句话总结:**
通过分析近三万次PR生命周期，提出协作型与辅助型AI编码代理谱系，揭示代理发起工作而人类保留合并决策的治理模式。

**Link:**
https://arxiv.org/abs/2605.08017

3. **Self-Play Enhancement via Advantage-Weighted Refinement in Online Federated LLM Fine-Tuning with Real-Time Feedback**

**Publish Date:**
2026-05-08

**一句话总结:**
针对联邦学习中资源受限边缘设备的LLM在线微调，该论文提出SPEAR，利用自对弈生成对比式提示对，通过最大似然和置信度加权非似然训练，仅需部分非答案反馈，在多个基准上验证了其优越性。

**Link:**
https://arxiv.org/abs/2605.07977

4. **DVD: Discrete Voxel Diffusion for 3D Generation and Editing**

**Publish Date:**
2026-05-08

**一句话总结:**
针对三维生成管线中的稀疏体素处理，该论文提出离散体素扩散框架DVD，将体素占据建模为离散变量以避免连续离散化阈值问题，实现生成、评估与编辑，利用预测熵量化不确定性，并通过块结构扰动微调支持单轮修复编辑。

**Link:**
https://arxiv.org/abs/2605.07971

5. **STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation**

**Publish Date:**
2026-05-08

**一句话总结:**
提出STARFlow2，基于自回归归一化流与预训练VLM交错融合的Pretzel架构，实现文本-图像统一生成，利用统一潜在空间和KV缓存，在生成与理解基准上取得竞争力性能。

**Link:**
https://arxiv.org/abs/2605.08029

6. **CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers**

**Publish Date:**
2026-05-08

**一句话总结:**
构建CoCoReviewBench基准，利用3900篇ICLR/NeurIPS论文及评审-讨论数据，通过完整性导向子集和正确性过滤评估AI评审，发现其正确性不足且易幻觉，推理模型表现更优。

**Link:**
https://arxiv.org/abs/2605.07905

7. **Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means**

**Publish Date:**
2026-05-08

**一句话总结:**
提出一种贝叶斯辅助的置信序列框架，利用工作预测模型自适应构造序列，在LLM评估等实验中能减少采样量并保持有效性。

**Link:**
https://arxiv.org/abs/2605.07964

8. **It Just Takes Two: Scaling Amortized Inference to Large Sets**

**Publish Date:**
2026-05-08

**一句话总结:**
针对摊销推断中部署集规模过大导致计算资源瓶颈的问题，该方法提出仅在大小不超过2的集合上训练均值池化深度集合编码器，然后微调推理头，使训练成本与部署集大小无关，在标量、图像、三维、分子等多类基准上表现相当或更好。

**Link:**
https://arxiv.org/abs/2605.07972

9. **LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling**

**Publish Date:**
2026-05-08

**一句话总结:**
这篇论文构建一个新的 benchmark，面向大模型能力评测；通过实验或基准测试验证方法是否真的改善任务表现；用途是给模型、agent 或工具链提供更可复现的横向比较标准。

**Link:**
https://arxiv.org/abs/2605.08083

10. **Similar Pattern Annotation via Retrieval Knowledge for LLM-Based Test Code Fault Localization**

**Publish Date:**
2026-05-08

**一句话总结:**
这篇论文整理一个新的数据集或任务集合，面向检索增强生成或复杂信息检索任务；通过实验或基准测试验证方法是否真的改善任务表现；用途是判断检索系统能否为复杂推理持续提供有效证据。

**Link:**
https://arxiv.org/abs/2605.07957
