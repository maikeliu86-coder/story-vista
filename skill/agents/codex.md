# Codex Adapter

Invocation: use `$story-vista` when installed, or run `python scripts/storyvista.py build input.txt --out output/story` in the repository.

Capabilities: file read/write and shell are expected; Browser should verify generated HTML when available; image generation remains optional.

Limit: preserve the dependency-free build path.

Mode: Core Skill Mode.

From the repository, run `python3 scripts/install_skill.py --target ~/.codex/skills/story-vista`, then invoke `$story-vista`. Do not copy only the `skill/` subdirectory: the installer packages the runtime and supporting files into one self-contained Skill directory. Codex should read the installed `SKILL.md`, create `visual-asset-plan.json`, create `image-manifest.json`, and only then build the final atlas.

Keep image generation optional and provider-neutral. Do not default to initials-only avatars.
