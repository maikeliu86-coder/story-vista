# Generic Agent Adapter

Invocation: run the CLI when shell access exists; otherwise follow the six-step workflow and emit schema-compatible JSON in order.

Capabilities: text generation is required; file, shell, browser, and image tools are optional.

Limit: missing capabilities select a fallback mode, not a fabricated success state.

Mode: Prompt-Only Mode, Project Instruction Mode, or AGENTS.md Mode.

If the agent cannot install a skill, paste the Required Workflow from `skill/SKILL.md`. Ask for these artifacts in order:

1. story data model
2. `visual-asset-plan.json`
3. `image-manifest.json`
4. optional semantic placeholders
5. final interactive atlas
6. verification checklist

Use this adapter for local LLM agents, OpenHands, DeepSeek-based agents, GLM-style agents, and other generic coding agents.
