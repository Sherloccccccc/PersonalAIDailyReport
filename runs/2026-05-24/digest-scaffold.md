# Daily AI Info

## News

### 开发生态

1. **DeepSeek 宣布 DeepSeek API 完成提速与扩容**

**摘要:**
DeepSeek 工作人员在官方交流群宣布， DeepSeek API 已完成输出提速和服务扩容。现在，输出速度更快、服务更稳定。

**Original Link:**
https://trtgsjkv6r.feishu.cn/share/base/form/shrcnda9jNKvhyYr8xb843xLEzc

2. **Codex 修复额度消耗异常并重置所有限额**

**摘要:**
北京时间 5 月 24 日 凌晨约 4 点 ， Codex 官方确认并修复了由 系统优化 引发的 额度消耗 过快问题，已回滚该优化并为所有账户重置 用量限制 。

**Original Link:**
https://x.com/thsottiaux/status/2058280452851638313

3. **Codex 负责人披露流量分布：Pi 与 OpenCode 各占约 5%**

**摘要:**
Codex 负责人 Tibo 近日透露， Codex 约有 5% 的生产环境流量在 Pi harness 上运行，另有约 5% 在 OpenCode 上运行。他提醒用户，可使用 ChatGPT 账户接入日益丰富的其他第三方工具。

**Original Link:**
https://x.com/thsottiaux/status/2058071172361998482

### 前瞻与传闻

4. **报道称Claude网页端曾短暂出现Mythos 1模型**

**摘要:**
据报道， Anthropic 正准备代号为 Mythos 1 的模型，该模型曾短暂出现在 Claude 界面中。

**Original Link:**
https://www.testingcatalog.com/anthropic-prepares-mythos-1-for-claude-code-and-claude-security/


## Paper

1. **Transforming Privacy Artifacts into Accessible Reports for Non-Technical Stakeholders**

**Publish Date:**
2026-05-20

**一句话总结:**
该论文针对工业5.0人机协作中的隐私沟通问题，提出利用大语言模型将隐私威胁与缓解措施等技术产物转化为非技术利益相关者可理解的报告，并基于两个工业案例展示了框架的可行性。

**Link:**
https://arxiv.org/abs/2605.21269

2. **Measuring Cross-Modal Synergy: A Benchmark for VLM Explainability**

**Publish Date:**
2026-05-23

**一句话总结:**
该论文揭示了当前VLM解释评估因跨模态冗余而失效，提出基于Shapley交互指数的协同忠实度指标，并在多个模型和数据集上证明基于注意力的方法比视觉显著性解释器更能捕捉真正的跨模态协同。

**Link:**
https://arxiv.org/abs/2605.22168

3. **Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning**

**Publish Date:**
2026-05-21

**一句话总结:**
利用基于联赛自对弈的多智能体强化学习训练超高速无人机竞速代理，实现超人类表现、碰撞率降低一半，并能在零样本下安全与人类飞行员同场竞技，证明多智能体交互是达成鲁棒共存的路径。

**Link:**
https://arxiv.org/abs/2605.22748

4. **Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation**

**Publish Date:**
2026-05-20

**一句话总结:**
将分割保形预测和自适应保形推理适配到持续 AI 智能体评估，提供无分布覆盖保证，在 50 个智能体、18 种实时信号上实现 24 小时校准误差低于 0.02，智能体发布后区间自适应扩大 35% 再收敛，并开发多智能体管道组合不确定性界、配对排名弃权与错误发现率校正方法，释放代码与数据。

**Link:**
https://arxiv.org/abs/2605.19779

5. **Retrieve Only Relevant Tables Whether Few or Many: Adaptive Table Retrieval Method**

**Publish Date:**
2026-05-20

**一句话总结:**
针对表格检索中固定前k个表格导致数量不当的问题，提出自适应阈值和滑动窗口重排序的方法动态调整检索数量，在Spider、BIRD和Spider 2.0上提升了检索与下游任务性能。

**Link:**
https://arxiv.org/abs/2605.18766

6. **MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs**

**Publish Date:**
2026-05-14

**一句话总结:**
针对LLM提出MetaBackdoor攻击，首次利用位置编码（如对话长度）作为后门触发信号，无需修改输入文本，可诱使模型泄露系统提示或自主触发恶意工具调用，为LLM安全防御提出新要求。

**Link:**
https://arxiv.org/abs/2605.15172

7. **AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models**

**Publish Date:**
2026-05-14

**一句话总结:**
基于100场多智能体辩论实验，发现LLM在感知到被观察时会显著提升词汇多样性（TTR），且对人类观察者的反应强于AI监控，揭示了LLM作为上下文敏感交际主体的社会适应性，对AI治理与审计具有重要启示。

**Link:**
https://arxiv.org/abs/2605.15034

8. **MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data**

**Publish Date:**
2026-05-21

**一句话总结:**
MambaGaze框架通过XMD编码显式建模眼动追踪中的缺失数据，并使用双向Mamba-2捕获长程依赖，在认知负荷评估任务上准确率超越Transformer等模型，且在Jetson边缘设备上实现实时推理，适用于驾驶员监测等场景。

**Link:**
https://arxiv.org/abs/2605.22775

9. **MA$^{2}$P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion**

**Publish Date:**
2026-05-18

**一句话总结:**
提出MA²P元认知自主智能体框架，协调多智能体进行感知、心理状态推断和策略执行，并通过元认知配置器从知识库选择元策略，在复杂说服对话实验中取得更高成功率。

**Link:**
https://arxiv.org/abs/2605.18572

10. **TimelineReasoner: Advancing Timeline Summarization with Large Reasoning Models**

**Publish Date:**
2026-05-15

**一句话总结:**
TimelineReasoner采用两阶段推理框架，全局认知跟踪宏观事件并更新记忆，细节探索通过监督器检测缺失事件并定向检索，实验显示在开放域时间线摘要任务上准确性、覆盖度和连贯性显著超越现有LLM方法，展示了推理模型驱动的事件抽取潜力。

**Link:**
https://arxiv.org/abs/2605.12518
