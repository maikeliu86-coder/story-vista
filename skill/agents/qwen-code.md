# Qwen Code Adapter

Invocation: read `AGENTS.md` and `skill/SKILL.md`, then run the repository CLI.

Capabilities: file read/write and shell are expected; Qwen Image is optional.

Limit: Chinese-provider availability does not change the provider-neutral core contract.

Mode: Project Instruction Mode or AGENTS.md Mode.

For Qwen Code and Tongyi-related coding agents, provide `AGENTS.md` and `skill/SKILL.md` as project instructions. For Qwen-Agent, use Framework Adapter Mode with schemas from `skill/templates/`.

Chinese image providers may include 通义万相 / Qwen Image, but StoryVista must also support manual assets and placeholder SVG output.
