# Story Interactive Archive

![Story Interactive Archive hero](assets/github-hero.png)

**Story Interactive Archive** is a Codex skill for turning novels, scripts, screenplays, and worldbuilding notes into durable interactive archive pages.

It grew out of a completed workflow for an Obsidian-based science-fiction archive: character relationship trees, character indexes, technology timelines, image-to-entity matching, mobile interaction, public static hosting, and real-time 3D space maps.

> Draft status: this repository is prepared for internal review. Do not publish, release, or make public until the owner confirms the content and presentation.

## What It Helps Build

- Obsidian-ready single-page interactive archives
- Character relationship trees with click-to-detail panels
- Character grids with bilingual names and portrait binding
- Technology and special-ability timelines
- Location, ship, planet, and route maps
- Real-time 3D space graphs with compressed story/world scale
- Image2 / GPT-Image generated assets matched one-to-one to story entities
- Public static pages that can be shared on mobile

## When To Use This Skill

Use this skill when a user asks to:

- turn a script or novel into an interactive archive
- organize story characters, places, technologies, and timelines
- generate and bind images for each story entity
- build a relationship tree or world map for a screenplay
- sync a local Obsidian HTML page with a public static website
- convert a flat story map into a true 3D spatial interface

## Install Locally

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-interactive-archive"
```

Then invoke it in a new Codex session:

```text
Use $story-interactive-archive to turn this new script into an Obsidian-ready interactive character, technology, and 3D space archive.
```

## Repository Layout

```text
.
├── README.md
├── README.zh-CN.md
├── assets/
│   └── github-hero.png
└── skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── implementation-notes.md
```

## Workflow Summary

1. Locate source text, Obsidian files, public HTML copies, and source records.
2. Read the story before classifying characters, ships, places, and technologies.
3. Build sections for character graphs, indexes, technology timelines, and space maps.
4. Generate or bind images one-to-one to the correct story entities.
5. Make interactions work on desktop and mobile.
6. Use real-time 3D geometry for spatial maps instead of flat image cards.
7. Verify local rendering, mobile behavior, and click-to-detail interactions.
8. Sync Obsidian, public copy, source record, and static hosting.

## Design Principles

- Preserve story evidence over visual convenience.
- Do not classify ships or places as characters.
- Do not paste 2D images as fake 3D cards when a 3D space map is requested.
- Prefer compressed story/world scale to equal spacing.
- Keep public sharing links distinct from local `file://` Obsidian paths.
- Verify every visual and interactive claim before final delivery.

## Internal Review Checklist

- [ ] The English README is accurate.
- [ ] The Chinese README is accurate.
- [ ] The hero image fits the GitHub details page.
- [ ] `skill/SKILL.md` describes the trigger conditions clearly.
- [ ] `skill/references/implementation-notes.md` captures the accepted workflow without overfitting to one book.
- [ ] The skill validates with `quick_validate.py`.
- [ ] The repository should remain private or draft until the owner approves publication.

## License

No public license is assigned yet. Keep this draft private until the owner chooses a license and publication policy.
