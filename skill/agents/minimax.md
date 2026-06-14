# MiniMax Adapter

Invocation: provide the Skill as project instructions or run the CLI when a local shell is available.

Capabilities: prompt execution is required; file/shell and MiniMax image tools are optional.

Limit: external image generation must update the manifest rather than bypass it.

Mode: Project Instruction Mode, Prompt-Only Mode, or BYO Image Model Mode.

Use StoryVista's core workflow to generate the story model, visual asset plan, prompts, and manifest. If MiniMax image generation is available, use `provider: "minimax-image"` in the manifest. If not, keep prompts ready and bind semantic placeholders.
