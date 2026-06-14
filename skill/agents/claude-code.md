# Claude Code Adapter

Invocation: `python scripts/storyvista.py build input.txt --out output/story`.

Capabilities: file read/write and shell are expected; browser and image tools are optional.

Limit: do not replace the portable CLI with platform-specific orchestration.

Mode: Project Instruction Mode.

Ask Claude Code to read `AGENTS.md` and `skill/SKILL.md` as project instructions. If Claude Code cannot install StoryVista as a native skill, paste the Required Workflow into the task prompt.

Required artifacts: story data model, `visual-asset-plan.json`, `image-manifest.json`, and final atlas when requested.
