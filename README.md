🌐 **English** · [简体中文](README.zh-CN.md)

<p align="center">
  <img src="docs/assets/brand-header.svg" width="860" alt="AI Context Linker — purple starlight wordmark and connected-link logo">
</p>

<p align="center">
  <a href="https://github.com/xhonye/AI-Context-Linker/actions/workflows/ci.yml"><img src="https://github.com/xhonye/AI-Context-Linker/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" alt="Python 3.11+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
</p>

**Give ChatGPT the project context. Bring the chosen plan back to Codex.**

Before changing any code, you may spend a long conversation in Codex understanding the project, comparing features, or deciding what to tackle first. Switching to ChatGPT means explaining the background and gathering files again.

**AI Context Linker prepares that context.** It turns selected local documents and reviewed project state into `ai_context.md`. Share it with ChatGPT to compare options, then bring the chosen plan to Codex for code-level verification and implementation. Reuse the briefing across project discussions.

No MCP server or whole-repository upload is needed for this file-based workflow. For people building local projects with a coding agent; installation currently uses an agent or CLI.

[Ask your agent to install](#ask-your-agent-to-install) · [See a generated briefing](docs/demo-ai-context.md) · [Connect a real project](INSTALL.md#4-connect-one-real-project-when-requested)

## Ask your agent to install

Copy this to an agent that can execute commands on your computer:

```text
Install https://github.com/xhonye/AI-Context-Linker after reading its INSTALL.md.
Check prerequisites, use an isolated installation, run the built-in demo,
and open the generated ai_context.md for me.
Proceed with installation and the synthetic demo; do not scan my real projects or upload.
Then help me connect one project: handle the configuration and let me review
which information will be shared and the resulting briefing.
```

The [agent installation guide](INSTALL.md) covers prerequisites, installation, verification, failures, and removal. Real project use still requires your selection and content review.

**Prefer commands?** With [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git available, uv can provision an isolated Python 3.11 environment:

```sh
uv tool install --python 3.11 git+https://github.com/xhonye/AI-Context-Linker.git
ai-context-linker demo --output-dir ./linker-demo
```

Run the demo from a local directory outside repositories. The output directory must be new. Open the printed `ai_context.md` path. The fictional demo reads no real projects. The current demo and generated headings are in Chinese.

## Discuss the direction, then implement

| What you want to do | How the tools work together |
|---|---|
| Decide which project to advance | Linker prepares approved goals, blockers, and next actions for discussion in ChatGPT |
| Compare options before coding | Share the briefing, discuss trade-offs, and identify missing evidence |
| Implement the chosen plan | Codex checks the actual code, makes changes, and validates them |

Local documents → **Linker briefing** → **ChatGPT discussion** → **Codex verification and implementation**.

This can move repeated context-setting and planning out of Codex. Actual savings depend on the task; no quota-saving percentage is promised. Use ordinary Chat for this workflow: [ChatGPT Work shares usage with Codex](https://learn.chatgpt.com/docs/pricing). Agent-assisted preparation and subsequent development have their own usage.

## Use your own project

1. **Choose one project.** Tell your agent its path and which documents may be shared. The agent handles configuration.
2. **Review the briefing.** Check the project description, goals, blockers, and next actions before approving sharing.
3. **Bring it to chat.** Upload the reviewed `ai_context.md` and ask what is blocked and what to do next.
4. **Bring the plan back.** Have Codex check the selected plan against the actual code before implementing and validating it.

Start with manual upload. Optionally place reviewed output in a dedicated synced folder and use a Drive connection supported by your account. **Linker does not log into or automatically upload to Google Drive.**

## After installation: everyday use

Once your own project is connected, tell your agent whenever local progress changes:

> Update ai_context

Your agent reuses the existing configuration, gathers updated information, helps you review the changes, and generates a fresh **`ai_context.md`**. Give that file to ChatGPT and continue the conversation.

Try: “Based on the latest progress, what should I do next?” No reinstall or repeated project introduction is needed. See the [technical workflow](docs/reference.md#quick-start).

## Community conversation

In [his Chinese-language article](https://mp.weixin.qq.com/s/abqrwY1T1WieYW5xDFKRRg), Khazix described planning in ChatGPT and implementing with Codex. I shared my small experiment with file-based project context in the comments and was delighted when he replied “也是个好思路！” (“That's a good approach too!”). See the [comment screenshot](docs/assets/khazix-comment-20260917.png).

The article's MCP setup queries live production data. Linker prepares a reviewable snapshot of selected project information. It can support a planning discussion; it does not provide live database, log, or runtime-metric access.

Thank you, Khazix, for the encouragement and for helping people discover this small project! I also recommend checking out his open-source [Khazix Skills](https://github.com/KKKKhazix/khazix-skills).

## Scope and privacy

- The local compiler makes no model API calls and has no third-party Python runtime dependencies. Installation downloads and your agent's own operation are separate.
- New projects are excluded by default. Only explicitly permitted information is collected; source-code bodies and raw conversations are outside the default scan.
- Sensitive-data checks help, but project descriptions can themselves be sensitive. Review before sharing.
- Missing progress remains unknown. A briefing does not fill gaps in production data or automatically update every conversation.
- Default briefings may reference project shards. Enable approved document attachments for a self-contained upload. The built-in demo is already self-contained.

## Evidence and limits

In limited maintainer trials, supplying reviewed business details reduced answer omissions. These are not independent benchmarks or guarantees: [observations and limits](docs/question-test-observations.md).

Use Linker for project discussion and context handoff. Use an engineering agent for implementation work. Linker does not synchronize all conversations or decide project priorities.

<details>
<summary>Earlier anonymized result cards (Chinese)</summary>

These AI-redrawn cards summarize anonymized observations, not original chat evidence. See the conditions and limitations linked above.

![Round one: missing evidence can lead to redundant development advice](docs/assets/round-1-anonymized.png)

![Round two: reviewed business evidence supports more grounded answers](docs/assets/round-2-anonymized.png)

</details>

## More

[Commands and configuration](docs/reference.md) · [Security boundary](docs/security-boundary.md) · [Architecture](docs/architecture.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)

Stuck? [Tell us which step failed](https://github.com/xhonye/AI-Context-Linker/issues/new/choose). If it saves you repeated project introductions, a Star helps others find it.
