# Daily AI Info

## News

### 开发生态

1. **Codex发布更新：自定义快捷键、Git优化与大幅性能提升**

**摘要:**
Codex 发布多项功能与性能改进，现已支持自定义键盘快捷键、优化 Git 操作并提升线程面板和本地服务器列表体验，官方称大型仓库下 Git 操作提速约 10 至 50 倍，线程切换重渲染减少约 75% 。

**Original Link:**
https://x.com/OpenAIDevs/status/2055717793841221796

2. **Codex 修复 GPT-5.5 性能下降问题并重置付费用户额度**

**摘要:**
针对用户反馈， Codex 团队确认已修复导致 GPT-5.5 能力下降的两个问题，并于北京时间 17日 凌晨宣布已重置所有付费计划的使用额度。

**Original Link:**
https://x.com/thsottiaux/status/2055707616605835333

3. **Vercel Labs 推出面向 Agent 的实验性编程语言 Zero**

**摘要:**
Vercel Labs 宣布推出一款专为 AI Agent 打造的实验性编程语言 Zero ，提供显式能力与 JSON 诊断。官方强调尚未稳定，主要供开发者试用和反馈。

**Original Link:**
https://github.com/vercel-labs/zero

### 产品应用

4. **微信读书推出 AI 助手 Skill**

**摘要:**
微信读书新增 AI 助手 Skill ，用户连接账号后可用 AI 搜书、导出笔记及分析阅读数据。

**Original Link:**
https://weread.qq.com/r/weread-skills

### 行业动态

5. **OpenAI 与马耳他政府合作向完成培训的公民提供一年免费 ChatGPT Plus**

**摘要:**
OpenAI 与 马耳他政府 宣布达成合作。 马耳他 公民在完成当地大学开发的 AI 培训课程后，可获得为期一年的 ChatGPT Plus 免费使用权。

**Original Link:**
https://openai.com/index/malta-chatgpt-plus-partnership/

6. **上海电信上线Token算力服务及免费体验活动**

**摘要:**
据报道， 上海电信 发布多档大模型调用 Token 资费套餐， 1 元 可享 25 万 额度点，支持话费支付。同时，限量向 上海 手机号用户提供免费 2500 万 额度体验。

**Original Link:**
https://mp.weixin.qq.com/s/H8D6ClBheNj3a_Au-4LKQg


## Paper

1. **Orchard: An Open-Source Agentic Modeling Framework**

**Publish Date:**
2026-05-14

**一句话总结:**
Orchard开源框架提供轻量环境服务Orchard Env及三个Agent训练配方，通过轨迹蒸馏、信用分配SFT和平衡自适应RL训练编码、GUI和个人助理Agent，在SWE-bench Verified达67.5%、WebVoyager等GUI基准达74.1%，成为最强开源模型。

**Link:**
https://arxiv.org/abs/2605.15040

2. **MeMo: Memory as a Model**

**Publish Date:**
2026-05-14

**一句话总结:**
MeMo框架将新知识编码进独立记忆模型，保持LLM参数不变，支持即插即用，能处理跨文档关系并抗检索噪声，在BrowseComp-Plus、NarrativeQA和MuSiQue三个基准上取得强性能，适用于为LLM高效注入领域知识。

**Link:**
https://arxiv.org/abs/2605.15156

3. **Veritas: A Semantically Grounded Agentic Framework for Memory Corruption Vulnerability Detection in Binaries**

**Publish Date:**
2026-05-14

**一句话总结:**
Veritas框架结合静态切片、双视图LLM检测器和多智能体验证器，通过语义接地和运行时证据在二进制中检测内存破坏漏洞，在基准上达90%召回率，并实际发现Apple漏洞获CVE分配。

**Link:**
https://arxiv.org/abs/2605.15097

4. **From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents**

**Publish Date:**
2026-05-14

**一句话总结:**
提出将文本工具调用基准转换为音频的评估框架，利用TTS、说话人变化和环境噪声保持原始标注，在Confetti和When2Call上评估7个全模态模型，发现性能退化主要源于语音中参数理解错误，并提供与人类偏好一致的参考自由LLM评判协议。

**Link:**
https://arxiv.org/abs/2605.15104

5. **Concurrency without Model Changes: Future-based Asynchronous Function Calling for LLMs**

**Publish Date:**
2026-05-14

**一句话总结:**
AsyncFC 提出无需修改模型的异步函数调用执行层框架，通过将LLM解码与函数执行解耦并支持函数间并行，在标准与软件工程基准上显著降低端到端延迟且保持准确率，揭示LLM可基于符号未来进行推理的原生能力。

**Link:**
https://arxiv.org/abs/2605.15077

6. **ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both**

**Publish Date:**
2026-05-14

**一句话总结:**
ATLAS提出将单个离散功能词同时作为智能体操作和隐式视觉推理单元，无需中间视觉生成或架构修改，结合隐锚GRPO稳定训练，在多个基准上取得优异性能，为可扩展视觉推理提供新范式。

**Link:**
https://arxiv.org/abs/2605.15198

7. **From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG**

**Publish Date:**
2026-05-14

**一句话总结:**
GranuRAG针对多模态检索增强生成中粗粒度证据与细粒度查询不匹配问题，提出元素级检测、多粒度跨模态对齐和归因约束生成三阶段框架，并构建包含多视角地标标注的GranuVistaVQA基准，实验显示较基线提升29.2%，实现可验证的错误诊断。

**Link:**
https://arxiv.org/abs/2605.15019

8. **MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory**

**Publish Date:**
2026-05-14

**一句话总结:**
MemEye针对多模态智能体记忆提出视觉证据粒度和检索使用方式二维评估框架，构建涵盖8个生活场景的基准，并对13种记忆方法在4种视觉语言模型上进行评测，揭示当前架构在保留细粒度视觉细节和时间状态推理上的不足，为设计更强记忆机制提供指引。

**Link:**
https://arxiv.org/abs/2605.15128

9. **ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World**

**Publish Date:**
2026-05-14

**一句话总结:**
ML-Embed 提出三维Matryoshka学习框架，训练140M到8B参数的多语言嵌入模型，通过覆盖430项任务的评测在低资源语言上创下新纪录，并完全开源模型、数据与代码，为构建全球公平且高效的计算嵌入系统提供可复现方案。

**Link:**
https://arxiv.org/abs/2605.15081

10. **Is Grep All You Need? How Agent Harnesses Reshape Agentic Search**

**Publish Date:**
2026-05-14

**一句话总结:**
通过在116条LongMemEval样本上使用Chronos、Claude Code等代理框架比较grep与向量检索，发现grep通常准确率更高，但工具输出形式（内联/文件）与干扰上下文显著影响代理搜索表现，为代理检索策略选择提供实验依据。

**Link:**
https://arxiv.org/abs/2605.15184
