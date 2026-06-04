# StoryVista

## Cross-Agent Story Visualization Skill

![StoryVista hero: manuscripts turning into character maps, timelines, scene maps, and world atlases](assets/github-hero.png)

[![GitHub stars](https://img.shields.io/github/stars/maikeliu86-coder/story-vista?style=social)](https://github.com/maikeliu86-coder/story-vista/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/maikeliu86-coder/story-vista?style=social)](https://github.com/maikeliu86-coder/story-vista/forks)
[![Last commit](https://img.shields.io/github/last-commit/maikeliu86-coder/story-vista)](https://github.com/maikeliu86-coder/story-vista/commits/main)
[![Issues](https://img.shields.io/github/issues/maikeliu86-coder/story-vista)](https://github.com/maikeliu86-coder/story-vista/issues)

**StoryVista** is a Codex-first, cross-agent compatible story visualization skill for turning novels, scripts, screenplays, lore documents, and long-form prose into interactive visual story atlases.

Chinese name: **文景**  
Chinese tagline: **让文字世界看得见**

StoryVista helps readers, writers, screenwriters, actors, students, researchers, worldbuilders, and creative teams turn dense narrative material into character maps, relationship graphs, location maps, timelines, concept indexes, character cards, visual asset libraries, and interactive story maps.

[中文说明 / Chinese README](README.zh-CN.md)

## Positioning

StoryVista is not tied to one AI agent or one image model. Codex remains the first supported platform, but the core workflow is portable: a story visualization protocol, cross-agent adapters, and a pluggable image-provider system.

Different agents have different native extension formats. StoryVista therefore provides a portable core workflow and platform-specific adapters rather than pretending that every platform installs skills in exactly the same way.

## What StoryVista Creates

- Character portraits, character cards, aliases, roles, arcs, and relationship maps
- Location key art, location cards, routes, maps, and 3D spatial nodes
- Faction and organization indexes with emblems
- Object, clue, motif, technology, magic-system, and concept indexes
- Event timelines, plot phase timelines, and event keyframes
- `story-atlas.json`, `image-manifest.json`, and an optional interactive HTML atlas
- Semantic SVG placeholders when no image model or user assets are available

## Supported Inputs

StoryVista works with novels, scripts, screenplays, RPG settings, worldbuilding notes, lore bibles, character sheets, location notes, timelines, research notes, long-form prose, and mixed Chinese/English source material.

## Supported Outputs

- Interactive single-page story atlas
- Obsidian-ready local archive
- Static-site-ready HTML
- Structured story model JSON
- Visual asset plan JSON
- Image manifest JSON
- Provider-specific image prompts
- Placeholder SVG asset set
- Framework adapter payloads for agent pipelines

## Supported Agents And Integration Modes

StoryVista can be used through several modes:

- **Core Skill Mode**: OpenAI Codex and agents that can install or read `skill/SKILL.md`.
- **Project Instruction Mode**: Claude Code, Cursor, Windsurf, OpenCode, GitHub Copilot Agent Mode, Qwen Code, Baidu Comate, and generic coding agents that read repository instructions.
- **AGENTS.md Mode**: Coding agents that automatically read project-level `AGENTS.md`.
- **Prompt-Only Mode**: Chat agents that cannot install a skill but can follow a copied workflow prompt.
- **Framework Adapter Mode**: Hugging Face smolagents, LlamaIndex, LangChain, CrewAI, AutoGen, Qwen-Agent, and custom Python pipelines.
- **BYO Image Model Mode**: Users generate images outside the agent, then bind them through `image-manifest.json`.
- **Manual Asset Binding Mode**: Users provide stills, screenshots, concept art, portraits, or folder-based assets.
- **No-Image Mode**: StoryVista emits prompts, manifest entries, and semantic SVG placeholders.

Platform notes are in [skill/references/cross-agent-compatibility.md](skill/references/cross-agent-compatibility.md) and [skill/agents/](skill/agents/).

## Image Provider System

StoryVista defines what images are needed; it does not force where they are generated. The core skill is image-provider neutral and supports bring your own image model workflows.

Supported provider modes include `openai`, `chatgpt-image`, `midjourney`, `stable-diffusion`, `flux`, `comfyui`, `minimax-image`, `qwen-image`, `tencent-hunyuan-image`, `baidu-wenxin-image`, `ideogram`, `leonardo`, `local-folder`, `manual-assets`, `placeholder-svg`, and `custom-api`.

If no provider is available, StoryVista still creates a complete visual asset plan, image prompts, an `image-manifest.json`, and semantic placeholders. Users can later generate images with Midjourney, Flux, Stable Diffusion, ComfyUI, MiniMax, Jimeng, Qwen Image / 通义万相, Tencent Hunyuan Image / 腾讯混元生图, Baidu Wenxin Image / 文心一格, OpenAI image models, or any custom tool.

See [skill/references/image-provider-guide.md](skill/references/image-provider-guide.md).

## No Initials-Only Avatar Policy

StoryVista must not use initials-only avatars as the default visual output. Every major character needs a planned `character_portrait` asset, and every key location needs a planned `location_keyart` asset. Images are bound through `image-manifest.json`.

Initials-only avatars are allowed only as a last-resort fallback when `allow_initials_avatar: true` is explicitly set. The default is `allow_initials_avatar: false`.

## Installation For Codex

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-vista"
```

Then invoke it:

```text
Use $story-vista to turn this novel, script, or long-form text into an interactive visual atlas with a visual asset plan and image manifest.
```

## Use With Claude Code

Claude Code may not install `SKILL.md` as a native skill in every environment. Use Project Instruction Mode:

1. Keep this repository in the project.
2. Ask Claude Code to read `AGENTS.md` and `skill/SKILL.md`.
3. Use `skill/agents/claude-code.md` as the adapter prompt.
4. Require `visual-asset-plan.json` and `image-manifest.json` before HTML generation.

## Use With Qwen Code And Chinese Agents

For Qwen Code, Qwen-Agent, MiniMax, Tencent Hunyuan, Tencent Cloud Agent Development Platform, Baidu Wenxin AgentBuilder, Baidu Comate, GLM, DeepSeek-based local agents, OpenHands, and other Chinese coding agents, use AGENTS.md Mode, Project Instruction Mode, Prompt-Only Mode, or Framework Adapter Mode. Chinese platform notes are in the adapter files under `skill/agents/`.

## Use With MiniMax

Use MiniMax through Project Instruction Mode, Prompt-Only Mode, or BYO Image Model Mode. Ask the agent to follow `skill/agents/minimax.md`, generate `visual-asset-plan.json`, and register any MiniMax-generated images with `provider: "minimax-image"` in `image-manifest.json`.

## Use With Generic Agents

If an agent cannot install skills, paste the required workflow from `skill/SKILL.md`, attach the source text, and ask for:

1. Entity extraction
2. Importance classification
3. Story data model
4. Visual asset plan
5. Image prompts or images
6. Image manifest
7. Final atlas
8. Verification checklist

## Use With Frameworks

For Hugging Face smolagents, LlamaIndex, LangChain, CrewAI, and AutoGen, treat StoryVista as a workflow spec plus schemas. Use the schemas in `skill/templates/` as tool input/output contracts, then bind the final artifacts into your pipeline.

## Bring Your Own Image Model

Configure a provider using [skill/templates/image-provider.config.example.yaml](skill/templates/image-provider.config.example.yaml), or keep provider output manual. StoryVista can produce model-neutral prompts first, then optional provider-specific prompt variants.

## Bring Your Own Images

Place user-provided images in a stable folder such as `assets/images/`, add them to `image-manifest.json` with `status: "user_provided"`, and bind each asset to character cards, relationship graph nodes, location cards, timelines, and 3D map nodes.

## Placeholder Mode

When no image tool is available, StoryVista creates semantic SVG placeholders that include full entity name, entity type, asset type, and visual category. These placeholders are tracked in `image-manifest.json`; they are not silent initials avatars.

## Example Workflows

- Minimal novel demo: [skill/examples/minimal-novel-demo](skill/examples/minimal-novel-demo)
- Screenplay workflow placeholder: [skill/examples/screenplay-demo](skill/examples/screenplay-demo)
- Bring-your-own-images workflow placeholder: [skill/examples/bring-your-own-images-demo](skill/examples/bring-your-own-images-demo)

## Repository Layout

```text
story-vista/
├── README.md
├── README.zh-CN.md
├── AGENTS.md
├── llms.txt
├── skill/
│   ├── SKILL.md
│   ├── agents/
│   ├── references/
│   ├── templates/
│   └── examples/
├── docs/
└── assets/
```

## Roadmap

- More complete framework adapters and runnable Python examples
- Provider-specific prompt translators
- HTML atlas starter templates
- More demos for screenplays, RPG settings, and bilingual novels
- Validation helpers for `story-atlas.json` and `image-manifest.json`
- Better manual asset review workflows

See [docs/roadmap.md](docs/roadmap.md).

## Limitations

- Long works may need chunking and iterative review.
- Entity extraction can be difficult with aliases, unreliable narration, nonlinear timelines, and ambiguous places.
- Generated images require human review before publication.
- StoryVista does not grant rights to copyrighted source material or generated images.
- Different platforms expose different agent, file, and image APIs; adapters describe integration patterns, not guaranteed one-click installation.

## Contributing

Contributions are welcome: adapters, examples, schemas, docs, prompts, provider guides, bug reports, and real use cases. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

## Security And Privacy

Do not paste private manuscripts, unpublished scripts, NDA materials, API keys, sensitive personal data, or local file paths into public issues. See [SECURITY.md](SECURITY.md).

## License

MIT License. See [LICENSE](LICENSE).
