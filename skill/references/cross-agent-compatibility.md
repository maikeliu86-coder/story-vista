# Cross-Agent Compatibility

Different agents have different native extension formats. StoryVista therefore provides a portable core workflow and platform-specific adapters rather than pretending that every platform installs skills in exactly the same way.

## Core Skill Mode

Use this mode for agents that can install or directly read `skill/SKILL.md`. OpenAI Codex is the first supported platform.

## Project Instruction Mode

Use this mode for Claude Code, Cursor, Windsurf, OpenCode, GitHub Copilot Agent Mode, Qwen Code, Baidu Comate, and similar coding agents. Add `skill/SKILL.md` to project instructions or ask the agent to read it before work begins.

## AGENTS.md Mode

Use root `AGENTS.md` for agents that automatically read repository instructions. This mode gives a compact workflow and points to the full references.

## Prompt-Only Mode

Use this mode for web chat agents and platforms without local file access. Paste the Required Workflow from `skill/SKILL.md`, then ask for `visual-asset-plan.json`, `image-manifest.json`, and the final atlas.

## Framework Adapter Mode

Use schemas in `skill/templates/` as contracts for Hugging Face smolagents, LlamaIndex, LangChain, CrewAI, AutoGen, Qwen-Agent, or custom Python agents. The framework should implement each StoryVista phase as a tool step or chain node.

## BYO Image Model Mode

Use this when users generate images outside the agent with Midjourney, Flux, Stable Diffusion, ComfyUI, MiniMax, Jimeng, Qwen Image, Tencent Hunyuan Image, Baidu Wenxin Image, OpenAI image models, or any custom provider.

## Manual Asset Binding Mode

Use this when users already have screenshots, stills, portraits, location images, or concept art. Register each file in `image-manifest.json` with `status: "user_provided"` and bind it to atlas targets.

## No-Image Mode

Use this when no provider or user image is available. Generate full prompts, image manifest entries, and semantic SVG placeholders with full entity names and types. Do not default to initials-only avatars.

## Platform Coverage

- OpenAI Codex: Core Skill Mode.
- Claude Code: Project Instruction Mode plus `skill/agents/claude-code.md`.
- GitHub Copilot / Agent Mode: AGENTS.md Mode or Project Instruction Mode.
- Cursor: AGENTS.md Mode or Project Instruction Mode.
- Windsurf / OpenCode / generic coding agents: AGENTS.md Mode.
- Hugging Face smolagents: Framework Adapter Mode.
- LlamaIndex: Framework Adapter Mode.
- LangChain: Framework Adapter Mode.
- CrewAI: Framework Adapter Mode.
- AutoGen: Framework Adapter Mode.
- Generic Local LLM Agent: Project Instruction Mode or Prompt-Only Mode.
- Generic Prompt-Only Agent: Prompt-Only Mode.
- Qwen Code / 通义千问 coding agents: Project Instruction Mode.
- Qwen-Agent: Framework Adapter Mode.
- MiniMax coding agents / MiniMax skills: Project Instruction Mode or Prompt-Only Mode.
- Tencent Hunyuan: Prompt-Only Mode or provider-specific image mode.
- Tencent Cloud Agent Development Platform: Project Instruction Mode or Framework Adapter Mode.
- Baidu Wenxin AgentBuilder: Prompt-Only Mode or project workflow mode.
- Baidu Comate / 文心快码: Project Instruction Mode.
- GLM Agent: Prompt-Only Mode or Project Instruction Mode.
- DeepSeek-based local agent / OpenHands / generic Chinese coding agents: AGENTS.md Mode or Prompt-Only Mode.
