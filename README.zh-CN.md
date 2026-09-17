🌐 [English](README.md) · **简体中文**

<p align="center">
  <img src="docs/assets/brand-header.svg" width="860" alt="AI Context Linker：紫色星光字标与链条标识">
</p>

<p align="center">
  <a href="https://github.com/xhonye/AI-Context-Linker/actions/workflows/ci.yml"><img src="https://github.com/xhonye/AI-Context-Linker/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" alt="Python 3.11+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
</p>

**让 ChatGPT 看懂项目，把 Codex 留给开发执行。**

代码还没开始改，你已经和 Codex 聊了很久：现状是什么、先做哪个功能、几个项目能不能合并。想换到 ChatGPT 继续讨论，又得重新介绍背景、整理文件。

**AI Context Linker 帮你准备这份背景资料。** 把选定的本地项目说明和经核对的进展整理成一份 `ai_context.md`，交给 ChatGPT 分析、比较方案；选好方向后，再让 Codex 核验并实施。换个聊天，也不用从头介绍几个项目。

不用先搭 MCP 服务，也不用上传整个代码仓库。适合用 Codex 等本地 AI agent 做项目的人；目前通过 agent 或命令行安装。

[让 AI agent 帮你安装](#让-ai-agent-帮你安装) · [先看生成的简报](docs/demo-ai-context.md) · [接入第一个项目](docs/quickstart-zh-CN.md)

## 让 AI agent 帮你安装

把下面这段复制给能在你电脑上执行命令的 AI agent：

```text
请安装 https://github.com/xhonye/AI-Context-Linker ，先阅读仓库的 INSTALL.md。
检查环境，采用隔离安装，再运行内置 demo，把生成的 ai_context.md 打开给我看。
安装和演示可以直接完成；演示不扫描我的真实项目，不上传。
然后帮我选一个真实项目接入：配置由你处理，我只核对分享范围和简报内容。
```

[安装说明（给 agent）](INSTALL.md)包含环境检查、安装、演示、失败处理和卸载。首次真实使用仍需你指定项目并核对内容。

**自己执行命令？** 需要 [uv](https://docs.astral.sh/uv/getting-started/installation/) 和 Git；uv 可准备 Python 3.11 的隔离环境：

```sh
uv tool install --python 3.11 git+https://github.com/xhonye/AI-Context-Linker.git
ai-context-linker demo --output-dir ./linker-demo
```

从仓库之外的本地目录运行演示，输出目录必须是新的。打开打印出的 `ai_context.md` 即可看到结果。演示使用虚构项目，不读取你的文件。

## 先聊清楚，再动手

| 你现在想做什么 | 怎么配合 |
|---|---|
| “这几个项目，今天先推进哪个？” | Linker 整理已批准的目标、卡点和下一步，ChatGPT 帮你比较 |
| “先别写代码，帮我看看方案。” | 把简报交给 ChatGPT，先讨论取舍和缺少的证据 |
| “方向定了，开始做。” | 把选定方案交给 Codex，核对实际代码后实施、验证 |

本地资料 → **Linker 简报** → **ChatGPT 讨论方案** → **Codex 核验、开发**。

希望少在 Codex 中反复梳理背景、讨论方向，可以从这一步开始。实际节省取决于任务；Linker 不承诺额度节省比例。这里指普通 Chat：[ChatGPT Work 与 Codex 共享用量](https://learn.chatgpt.com/docs/pricing)，整理资料的 agent 和后续开发也有各自用量。

## 从演示到自己的项目

1. **选一个项目。** 告诉 agent 项目路径和允许分享的文档；它负责配置。
2. **核对简报。** 检查项目说明、目标、卡点与下一步，确认哪些内容可以分享。
3. **交给聊天。** 上传审核后的 `ai_context.md`，问“目前卡在哪里，下一步是什么？”
4. **把方案带回去。** 选定方向后，让 Codex 对照实际代码核验，再实施和验证。

先用手动上传跑通。需要 Drive 时，再把审核后的输出放到专用同步目录，使用账号支持的连接方式。**Linker 不负责登录或自动上传 Google Drive。**

## 安装好后怎么用？

首次接入自己的项目后，本地项目有了新进展，就跟你的 agent 说：

> 更新 ai_context

agent 会沿用已有配置整理最新资料，带你核对变化，再生成新版 **`ai_context.md`**。把这个文件交给 ChatGPT，就可以接着聊了。

比如问：“按最新进展，我下一步应该做什么？”不用重新安装，也不用每次从头介绍项目。详见[中文上手指南](docs/quickstart-zh-CN.md)。

## 从数字生命卡兹克的文章来？

卡神在[这篇文章](https://mp.weixin.qq.com/s/abqrwY1T1WieYW5xDFKRRg)里分享了“ChatGPT 分析规划、Codex 开发执行”的工作流。我也在留言区分享了自己用项目简报衔接上下文的小尝试，没想到收到了卡神的回复：**“也是个好思路！”**（第一次被卡神回复，感动！[留言截图](docs/assets/khazix-comment-20260917.png)）

文章中的 MCP 用来按需查询真实生产数据；Linker 则提供可审阅的项目资料快照。想先带着项目背景聊方案，可以从简报开始；需要最新数据库、日志或运行指标，仍需另接数据来源。

感谢卡神的分享和鼓励，让更多人看到了这个小项目！也推荐大家去看看他的开源项目 [Khazix Skills](https://github.com/KKKKhazix/khazix-skills)。

## 读取与分享范围

- 本地编译器不调用模型 API；零第三方 Python 运行时依赖。安装下载和 agent 自身运行另计。
- 新项目默认不导出；只收集明确允许的资料，默认不读取源码正文或原始聊天记录。
- 输出带敏感信息检查，但项目说明本身也可能敏感，分享前仍需核对。
- 没有记录的进展仍是未知；简报不会自动补齐生产数据，也不会让所有聊天自动更新。
- 默认简报可能引用项目分片；需要单文件上传时，按指南启用已批准文档附件。内置 demo 已是单文件可读。

## 效果和边界

维护者的有限自用对照中，补齐经核对的业务资料后，回答遗漏有所减少。这不代表独立评测或通用效果保证：[观察与局限](docs/question-test-observations.md)。

它适合项目讨论和上下文交接；读取实现、修改代码仍交给工程 agent。它不会实时同步所有聊天，也不替你决定项目优先级。

<details>
<summary>查看此前的匿名结果卡</summary>

以下为 AI 重新排版的匿名观察结果，不是原始聊天证据；完整条件与局限见上方说明。

![第一轮：缺失资料可能导致重复开发建议](docs/assets/round-1-anonymized.png)

![第二轮：补齐业务资料后，回答更有依据](docs/assets/round-2-anonymized.png)

</details>

## 更多资料

[详细命令与配置](docs/reference-zh-CN.md) · [安全边界](docs/security-boundary.md) · [架构](docs/architecture.md) · [贡献指南](CONTRIBUTING.md) · [MIT 许可](LICENSE)

试用遇到问题？[告诉我们卡在哪一步](https://github.com/xhonye/AI-Context-Linker/issues/new/choose)。如果它确实减少了你重复介绍项目的时间，欢迎点 Star。
