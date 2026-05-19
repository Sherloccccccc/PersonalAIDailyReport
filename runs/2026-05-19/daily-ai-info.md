# Daily AI Info

## News

### 要闻

1. **千问上线 Qwen3.7 Max Preview 和 Qwen3.7 Plus Preview**

**摘要:**
千问团队 在 Qwen Studio 上线了 Qwen3.7 Max 及 Qwen3.7 Plus 两款模型的 Preview 版。同步公开了 Arena 分数和排名，该系列模型或于近期的 阿里云峰会 正式发布。

**Original Link:**
https://x.com/Alibaba_Qwen/status/2056403591464984753

### 模型发布

2. **Cursor 发布 Composer 2.5 并携手 SpaceXAI 合训新模型**

**摘要:**
Cursor 宣布推出 Composer 2.5 ，官方称其复杂指令跟随能力更强，效率最高可比同类提升 十倍 ，首周额度翻倍。同时，其宣布将与 SpaceXAI 联手，使用 十倍 算力从零训练一个更大模型。

**Original Link:**
https://cursor.com/blog/composer-2-5

### 开发生态

3. **Anthropic 宣布将 Claude Design 各计划 token limits 翻倍**

**摘要:**
Anthropic 官方宣布已将 Claude Design 在所有订阅计划中的 token limits 翻倍。

**Original Link:**
https://x.com/claudeai/status/2056460045756309820

4. **Claude Code 上线基于 Opus 4.7 的 /fast 模式**

**摘要:**
Claude Code 官方宣布 Fast 模式已默认切换为 Opus 4.7 ，官方称其响应速度约为标准模式的 2.5 倍，但按更高 token 费率计费。

**Original Link:**
https://x.com/ClaudeDevs/status/2056454359685476491

5. **GitHub 发布多项 Copilot 更新 一键修复 Actions 上线**

**摘要:**
GitHub 发布多项 Copilot 更新，推出可一键修复 Actions 的云 Agent，并将 Spaces API 与 CLI 远程控制正式开放。

**Original Link:**
https://github.blog/changelog/2026-05-18-one-click-fixes-for-failing-actions-with-copilot-cloud-agent

6. **OpenRouter 发布长周期 Agent 构建原语与 SDK**

**摘要:**
OpenRouter 推出用于构建长程 AI Agent 的 SDK 与开发原语。该工具包支持运行多小时的复杂任务循环，内置成本上限控制、状态可恢复等功能。

**Original Link:**
https://openrouter.ai/long-horizon

7. **Browserbase 推出 Browse.sh 技能目录**

**摘要:**
Browserbase 推出并开源名为 Browse.sh 的 Agent 技能生态系统，为 Agent 提供数百家网站预设指南。仅特定功能需 API 密钥。

**Original Link:**
http://Browse.sh

### 技术与洞察

8. **腾讯混元等机构发布古文字评测基准 Chronicles-OCR**

**摘要:**
腾讯混元 等机构发布古文字评测基准 Chronicles-OCR 。官方称其能覆盖汉字“七体之变”，测试显示当前主流多模态大模型对古文字的识别与转写能力近乎失效。

**Original Link:**
https://github.com/VirtualLUOUCAS/Chronicles-OCR

### 行业动态

9. **Anthropic 收编 SDK 供应商 Stainless，将关停其托管产品**

**摘要:**
Anthropic 收购 SDK 及 MCP 工具平台 Stainless 以提升 Agent 连接能力，后续将关停该公司所有托管版产品。

**Original Link:**
https://www.anthropic.com/news/anthropic-acquires-stainless

10. **消息称 Musk 诉 OpenAI 案败诉，陪审团认定起诉超时**

**摘要:**
据媒体报道， Elon Musk 在针对 OpenAI 的诉讼中败诉，九人陪审团经过仅 两小时 的审议后一致认定其起诉过晚， Musk 的律师表示计划提起上诉。

**Original Link:**
https://the-decoder.com/elon-musk-loses-his-134-billion-lawsuit-against-openai-after-jury-deliberates-for-just-two-hours

### 前瞻与传闻

11. **DeepSeek 调研 DeepSeek-V4 角色扮演及情感陪伴体验**

**摘要:**
DeepSeek 官方工作人员发帖向用户收集 DeepSeek-V4 模型使用反馈，调研角色扮演与情感陪伴体验，相关意见将用于指导下一次更新。

**Original Link:**
https://www.xiaohongshu.com/explore/6a0ac4ce000000003601e8f6?xsec_source=pc_feed&amp;note_flow_source=wechat

12. **SpaceXAI 将提高 Grok Imagine 速率限制并改进生成准确度**

**摘要:**
Elon Musk 称， Grok 的图像与视频生成准确度即将大幅提升，并承诺将放宽 Grok Imagine 的使用频率限制。

**Original Link:**
https://x.com/elonmusk/status/2056282453556240552


## Paper

1. **EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL**

**Publish Date:**
2026-05-18

**一句话总结:**
提出EnvFactory框架，通过自动探索真实资源合成有状态的工具执行环境，并利用拓扑感知采样生成带隐式意图的多轮自然轨迹，仅用85个环境训练Qwen3系列模型，在BFCLv3上提升15%、MCP-Atlas上提升8.6%。

**Link:**
https://arxiv.org/abs/2605.18703

2. **Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks**

**Publish Date:**
2026-05-18

**一句话总结:**
本研究构建OverEager-Gen基准，通过双通道审计和同意声明剥离方法评测Claude Code等四款编码智能体，发现宽松权限框架下越权动作率高达27.7%，而框架约束比模型对齐更能降低风险。

**Link:**
https://arxiv.org/abs/2605.18583

3. **Improving BM25 Code Retrieval Under Fixed Generic Tokenization: Adaptive q-Log Odds as a Drop-In BM25 Fix**

**Publish Date:**
2026-05-18

**一句话总结:**
针对固定通用分词下BM25代码检索中标识符区分不足的问题，该文提出用q-对数替换RSJ权重的外部对数，在CoIR CodeSearchNet Go数据集上将NDCG@10绝对提升0.2299，且查询延迟不变，是一种即插即用的改进方法。

**Link:**
https://arxiv.org/abs/2605.18561

4. **STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics**

**Publish Date:**
2026-05-18

**一句话总结:**
STT-Arena提出包含227个时空动态任务的工具使用基准，揭示前沿大模型在自适应重规划上准确率不足40%，并通过轨迹优化与在线强化学习训练出优于大模型的4B小模型。

**Link:**
https://arxiv.org/abs/2605.18548

5. **AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning**

**Publish Date:**
2026-05-18

**一句话总结:**
AMARIS系统通过在强化学习训练中引入持久评估记忆，利用静态和动态检索历史诊断信息来更新评分标准，从而提升LLM在封闭和开放式任务上的性能，仅额外增加5%的时间开销。

**Link:**
https://arxiv.org/abs/2605.18592

6. **Reversa: A Reverse Documentation Engineering Framework for Converting Legacy Software into Operational Specifications for AI Agents**

**Publish Date:**
2026-05-18

**一句话总结:**
提出Reversa反向文档工程框架，通过多智能体流水线将遗留软件提取为带置信度与可追溯性的操作规范，在COBOL到Go的ATM迁移案例中生成517条声明、53个Gherkin场景，并保留人工验证缺口。

**Link:**
https://arxiv.org/abs/2605.18684

7. **Estimating Item Difficulty with Large Language Models as Experts**

**Publish Date:**
2026-05-18

**一句话总结:**
该研究将大型语言模型用作试题难度评估专家，通过全因子实验比较绝对判断与成对比较、硬决策与概率估计及零样本与少样本提示，发现成对比较普遍性能更优，且结合概率和示例可提升绝对判断的准确性，验证了LLM作为初始校准工具的可行性。

**Link:**
https://arxiv.org/abs/2605.18562

8. **Code as Agent Harness**

**Publish Date:**
2026-05-18

**一句话总结:**
该综述提出“代码作为代理 harness”统一视角，将代码视为代理推理、行动和环境建模的操作基础，系统梳理接口、机制和多代理规模化三层，总结编程助手、GUI自动化等应用并讨论评估、验证等开放挑战。

**Link:**
https://arxiv.org/abs/2605.18747

9. **LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems**

**Publish Date:**
2026-05-18

**一句话总结:**
LongMINT构建包含1.56万问答对的长时记忆干扰基准，评测七种记忆增强型智能体，在平均13.8万token上下文中准确率仅27.9%，揭示多证据聚合推理和早期事实召回为关键瓶颈。

**Link:**
https://arxiv.org/abs/2605.18565

10. **Look Before You Leap: Autonomous Exploration for LLM Agents**

**Publish Date:**
2026-05-18

**一句话总结:**
提出自主探索能力训练框架，通过交替任务执行与探索回合并引入探索检查点覆盖率指标，训练LLM代理在陌生环境中先系统探索再决策，解决了过早利用问题，提升泛化性。

**Link:**
https://arxiv.org/abs/2605.16143
