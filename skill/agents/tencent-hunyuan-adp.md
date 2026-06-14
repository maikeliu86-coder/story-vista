# Tencent Hunyuan / Tencent Cloud Agent Development Platform Adapter

Invocation: represent the six pipeline phases as workflow steps or call the CLI through an execution tool.

Capabilities: prompt execution and artifact storage are required; shell and image generation are optional.

Limit: generated images must record provider, status, path, alt text, and rights note in the manifest.

Mode: Prompt-Only Mode, Project Instruction Mode, or Framework Adapter Mode.

Use StoryVista phases as agent workflow steps. If Tencent Hunyuan image generation is available, record `provider: "tencent-hunyuan-image"`. If not, emit prompt-ready manifest entries and semantic placeholders.
