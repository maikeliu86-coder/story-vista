# Baidu Wenxin AgentBuilder Adapter

Invocation: provide `skill/SKILL.md` as project instructions; use the CLI only when file and shell tools are available.

Capabilities: prompt execution is required; file/shell and image tools are optional.

Limit: preserve evidence status and return schema-compatible artifacts even when the platform cannot write files.

Mode: Prompt-Only Mode or Project Instruction Mode.

Use StoryVista as a workflow prompt. If Wenxin image tools or 文心一格 are available, record the provider as `baidu-wenxin-image`; otherwise generate prompts and semantic placeholders.

Do not treat initials-only avatars as primary portraits.
