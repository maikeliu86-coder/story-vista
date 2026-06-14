# GitHub Copilot Agent Mode Adapter

Invocation: use `AGENTS.md` plus `skill/SKILL.md`, then run the repository CLI in the workspace terminal.

Capabilities: file read/write and shell are expected; browser and image tools are optional.

Limit: generated artifacts must remain reproducible from source and templates.

Mode: AGENTS.md Mode or Project Instruction Mode.

Use root `AGENTS.md` as the compact contract and `skill/SKILL.md` as the detailed workflow. Copilot Agent Mode should create `visual-asset-plan.json` and `image-manifest.json` before editing or generating atlas pages.
