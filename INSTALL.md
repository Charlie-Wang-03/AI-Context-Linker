# Install with your local AI agent

[中文首页](README.zh-CN.md) · [English overview](README.md)

This guide is for a local agent that can run terminal commands. A web chat without
access to your computer cannot perform this installation. Installing Linker does
not authorize scanning real projects, approving their contents, or uploading files.

## Copy this request / 复制给本地 AI agent

> 请安装 https://github.com/xhonye/AI-Context-Linker ，先阅读仓库的 INSTALL.md。
> 检查环境，采用隔离安装，再运行内置 demo，把生成的 ai_context.md 打开给我看。
> 安装和演示可以直接完成；演示不扫描我的真实项目，不上传。
> 然后告诉我如何选一个真实项目接入，配置由你处理，我只核对分享范围和简报内容。

## 1. Check the environment and existing installation

- Identify the OS and shell. Check `uv --version`, `git --version`, and
  `ai-context-linker --help` when those executables exist.
- Reuse a working installation. Inspect `uv tool list` before replacing a tool.
  Do not overwrite a developer checkout, remove files, or use `--force` to hide conflicts.
- Prefer `uv`: it installs Python tools into isolated environments. This is a Python
  CLI; Node and npm are not required. Python 3.11+ is required.
- If uv is missing, follow its [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
  using the platform's supported route. Report prerequisites or failures explicitly.
  Installation may download Python and packages; the compiler itself makes no network calls.

## 2. Install the reviewed repository version

With uv and Git available:

```sh
uv tool install --python 3.11 git+https://github.com/xhonye/AI-Context-Linker.git
ai-context-linker --help
```

For a reproducible install, append `@<reviewed-commit-sha>` to the Git URL, replacing
the placeholder with an actual verified commit. Do not invent a release or claim a
PyPI/npm publication. Record the installed source revision when available.

If the tool command is not on PATH, use `uv tool dir --bin` to find its executable
and call that absolute path for this session. Explain how to reopen the terminal;
do not repeatedly reinstall to solve a PATH issue.

For a reviewed local checkout (including unreleased onboarding changes):

```sh
uv tool install --python 3.11 /absolute/path/to/AI-Context-Linker
```

Use the actual OS-specific absolute path, quoted when it contains spaces.
If uv cannot be used but Python 3.11+ is available, create a dedicated virtual
environment and install the reviewed repository with that environment's
`python -m pip install <repository-or-checkout>`. Do not install globally or into
another project's environment. If Git is unavailable, use a downloaded and reviewed
checkout with the local-path route.

## 3. Produce the first result

Choose a **new, dedicated local output directory** outside project repositories,
private configuration directories, and existing publish/sync folders. Show its path.

```sh
ai-context-linker demo --output-dir /absolute/path/to/linker-demo
```

Use the actual path. Open the reported `ai_context.md` in an available file viewer.
The demo uses two fictional projects and a fixed, explicitly labelled snapshot.
It neither scans the workspace nor uploads, logs into Drive, records real approval,
or calls a model. It refuses an existing output directory; choose a fresh one.

Success means the **installed command** produced a readable single-file briefing,
with both projects' blockers and next actions visible. A successful package install
alone is insufficient. If `demo` is absent, report that the installed revision lacks
this feature; do not claim success or silently scan real projects instead.

The user may upload the fictional file and ask:

> 按这份演示快照，两个项目各卡在哪里、下一步是什么？缺少依据的地方请标为未知。

## 4. Connect one real project, when requested

Ask only for missing scope: the selected project path and which documents may be
shared. Reuse explicit authorization already given in the conversation. Do not
request every field separately or ask the user to hand-edit JSON.

1. Read [the configuration example](examples/synthetic-workspace-config.json),
   [the schema](schema/workspace-config.schema.json), and the
   [Chinese first-project guide](docs/quickstart-zh-CN.md). Make private configuration
   outside repositories and sync folders. Start with **one selected project**;
   do not discover the whole home/workspace or include skills by default.
2. Present the selected documents and intended sharing scope in plain language.
   Missing permission remains `deny`. For a single upload that must contain the
   selected documents, set `attach_files` to the approved subset of `allow_files`.
   This does not authorize source-code export or raw conversation collection.
3. Use `scan` to produce private review artifacts. Prepare current-state drafts
   only from available evidence; unknown goals, blockers and next actions stay
   unknown. Use `init-review-state` and `preview-review-state` as needed. The agent
   handles configuration; the user reviews the meaning and sharing scope.
4. After explicit approval of the concrete candidate/version, record it with
   `approve-snapshot`, then `build` into a dedicated output directory. Follow the
   [reference](docs/reference.md#quick-start); do not bypass failing checks.
5. Open `ai_context.md` and show what it contains. Let the user share the reviewed
   file manually first. Drive setup is optional and separate; do not claim Linker
   has authenticated, uploaded, or verified cloud sync.

For future refreshes, reuse the private configuration, scan the changes, preserve
previous approval history, and review the new candidate. Installing once does not
make subsequent conversations or local changes automatically available to Chat.

## 5. Handoff and removal

Report the installed command path, source revision if known, demo output path,
private configuration path if created, and any remaining prerequisite. Clearly
separate a synthetic demo from a real project trial and cloud delivery.

For a uv-managed installation, `uv tool uninstall ai-context-linker` removes the
tool when requested. It does not remove user configuration or generated briefings.
For a dedicated virtual environment, identify its path rather than deleting it
automatically. Do not install the optional repo Skill into user runtimes without
an explicit request.
