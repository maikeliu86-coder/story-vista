# Codex Adapter

Invocation: use `$story-vista` when installed, or run `python scripts/storyvista.py build input.txt --out output/story` in the repository.

Capabilities: file read/write and shell are expected; Browser should verify generated HTML when available; image generation remains optional.

Limit: preserve the dependency-free build path.

Mode: Core Skill Mode.

Install `skill/` into the Codex skills directory, then invoke `$story-vista`. Codex should read `skill/SKILL.md`, create `visual-asset-plan.json`, create `image-manifest.json`, and only then build the final atlas.

Keep image generation optional and provider-neutral. Do not default to initials-only avatars.
