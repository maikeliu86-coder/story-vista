# Quick Start

## What StoryVista Is

StoryVista turns a novel, screenplay, or story document into a spoiler-safe visual reading atlas. It extracts characters, locations, relationships, objects, factions, and events, then organizes them into a navigable HTML codex with evidence-aware notes and optional image workflows.

## Who It Is For

- Readers working through long or complex novels
- Book clubs that need a shared spoiler-safe reference
- Researchers and students studying story structure
- Writers and worldbuilding teams reviewing internal lore
- Agent users who want a repeatable workflow instead of manual note-taking

## What Problems It Solves

- Character overload: too many names, aliases, titles, or factions
- Place disorientation: hard to remember where scenes happen
- Lore drift: objects, technologies, powers, and world rules become hard to track
- Spoiler risk: readers need progress-aware summaries, not full-book spoilers
- Image workflow confusion: users need either real generated images or a clean prompt task list

## Install StoryVista In An Agent Workflow

StoryVista's stable interface is the local repository plus Python CLI. Different agents are orchestration layers on top of the same files.

### Codex

1. Open the repository in Codex.
2. Make sure Python is available in the workspace.
3. Ask Codex to run StoryVista on a text file or prompt it to inspect an existing `output/` directory.

### Claude Code

1. Open the same repository in Claude Code.
2. Run the documented CLI commands from the project root.
3. Use Claude Code to iterate on prompts, output review, and image-binding steps.

### Trae

1. Open the repository or import it into Trae.
2. Use Trae's terminal support to run `python scripts/storyvista.py ...`.
3. Review generated files and ask Trae to rebuild or refine the atlas.

### Marvis

1. Use Marvis only if it can read files, run shell commands, and keep a local working directory.
2. Point it at this repository and ask it to use the Python CLI rather than inventing a parallel workflow.
3. Treat any provider selection as user-confirmed guidance, not automatic paid generation.

### Cursor And Other Agents

1. Open the repository.
2. Run the CLI directly or ask the agent to run it.
3. Use the generated files in `output/<demo-or-project>/` as the source of truth.

If a tool supports Skill or Agent instructions but cannot run shell commands, it can still help draft prompts and review outputs, but the actual atlas build must happen in an environment that can execute Python.

## First Run

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
python scripts/storyvista.py validate output/reader-visual-codex-demo
```

Open `output/reader-visual-codex-demo/atlas.html` in a browser.

## How To Enter The First Task

The first task should specify:

- the source text
- the current reading boundary
- the need for spoiler-safe extraction
- whether images should be generated or only planned
- the preferred UI language

Good first tasks are concrete. Avoid vague requests like "summarize this book."

## How To Choose An Image Model

StoryVista is provider-neutral. It does not require one fixed image engine.

- Choose `Image2` when the current agent already has built-in image generation and you want a simple in-agent workflow.
- Choose `SeeDream` when you want a cloud workflow with prompt export and later manual binding.
- Choose `ComfyUI` when you want local node-based control and self-hosted model routing.
- Choose `Flux` when you want a modern local or hosted text-to-image model with strong realism and prompt fidelity.
- Choose `SDXL` when you want a broad local-model ecosystem and many existing checkpoints.

If the current agent cannot actually generate images, StoryVista should not pretend otherwise. It should output a structured generation task list instead of empty placeholders.

## How To Avoid Spoilers

- Tell StoryVista the current reading progress before extraction.
- Ask it to use only the source text up to that boundary.
- Keep later chapters out of the working input if possible.
- Lock or hide future relationships and events.
- Review the atlas before sharing it with other readers.

## If No Image Model Is Available

When no usable image model is detected, StoryVista should still produce:

- `visual-asset-plan.json`
- `image-manifest.json`
- `prompt-pack.md`
- provider-specific prompt files when requested
- a structured task list describing what should be generated for each character, place, object, or event

It should not claim that images already exist. It should not use blank output as if generation succeeded.

## Example English Prompt

```text
Use StoryVista to analyze this novel and build a spoiler-safe visual reading codex.

Requirements:
- Extract characters, locations, objects, factions, timeline events, and relationships
- Only use source text within the current reading progress
- Do not reveal later plot points
- If the current agent has a working image model, generate images
- If no working image model is available, output a structured image generation task list instead of blank placeholders
```

## 中文示例提示词

```text
请使用 StoryVista｜文景 分析这部小说，并生成防剧透的视觉阅读图鉴。

要求：
- 提取人物、地点、物品、阵营、时间线和人物关系
- 只根据当前阅读进度内的原文生成内容
- 不要提前剧透后文
- 如果当前 Agent 有可用生图模型，请生成图片
- 如果没有可用生图模型，请输出结构化的生图任务清单，不要输出空白占位图
```
