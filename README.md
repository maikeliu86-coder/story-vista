# StoryVista

![StoryVista hero](assets/github-hero.png)

**StoryVista** helps people make text worlds visible.

It is a Codex skill for turning novels, scripts, screenplays, long-form prose, roleplaying worlds, and dense story notes into interactive visual atlases. It is designed for readers, writers, screenwriters, students, researchers, and creative teams who need to understand complicated characters, scenes, timelines, concepts, and world relationships at a glance.

Chinese name: **文景**  
Tagline: **Make Text Worlds Visible** / **让文字世界看得见**

> Draft status: this repository is prepared for internal review. Do not publish, release, or make public until the owner confirms the content and presentation.

## Why StoryVista Exists

Long stories are hard to hold in your head. Characters change sides, scenes jump across places, important objects appear before their meaning is clear, and a screenplay can hide a large world behind short lines of dialogue.

StoryVista turns that text into an explorable interface:

- Who is connected to whom?
- Where does each scene happen?
- What events happen in what order?
- Which places, objects, powers, technologies, symbols, or factions matter?
- How can a reader or creative team quickly revisit the structure of the work?

## What It Helps Build

- Interactive character relationship trees
- Character or role indexes with portraits and summaries
- Scene, location, object, faction, and world maps
- Plot, technology, power, or motif timelines
- Image2 / GPT-Image visual assets matched one-to-one to story entities
- Mobile-friendly archive pages for readers and collaborators
- Obsidian-ready local pages plus optional public static sharing
- Real-time 3D maps for spatial stories, journeys, planets, cities, rooms, or worlds

## Who It Is For

- Novel readers who want to understand complex relationships
- Writers who want to see whether a story structure is coherent
- Screenwriters and producers tracking characters, scenes, and locations
- Students and teachers analyzing narrative works
- Worldbuilders managing factions, places, routes, and lore
- Researchers turning long narrative material into navigable knowledge

## Install Locally

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-vista"
```

Then invoke it in a new Codex session:

```text
Use $story-vista to turn this novel, script, or long-form text into an interactive visual atlas for characters, scenes, timelines, concepts, and world maps.
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

## Core Workflow

1. Locate the source text, notes, Obsidian files, public HTML copies, and source records.
2. Read the text before classifying characters, locations, objects, technologies, or factions.
3. Build sections around reader questions: people, places, time, concepts, and world structure.
4. Generate or bind images one-to-one to the correct story entities.
5. Make interactions work on desktop and mobile.
6. Use real-time 3D geometry for spatial maps when depth matters.
7. Verify local rendering, mobile behavior, and click-to-detail interactions.
8. Sync Obsidian, public copies, source records, and static hosting when requested.

## Design Principles

- Preserve textual evidence over decorative assumptions.
- Do not misclassify ships, cities, objects, or organizations as characters.
- Do not use fake 3D image cards when the user asks for a real spatial map.
- Use compressed story/world scale when true distances are too large.
- Keep public sharing links distinct from local `file://` paths.
- Verify every visual and interactive claim before delivery.

## Internal Review Checklist

- [ ] The name StoryVista / 文景 feels clear and memorable.
- [ ] The English README speaks to a broad audience, not one specific novel.
- [ ] The Chinese README speaks to readers, writers, screenwriters, and worldbuilders.
- [ ] The hero image fits the GitHub details page.
- [ ] `skill/SKILL.md` describes trigger conditions clearly.
- [ ] `skill/references/implementation-notes.md` captures reusable workflow details.
- [ ] The skill validates with `quick_validate.py`.
- [ ] The repository remains private or draft until the owner approves publication.

## License

No public license is assigned yet. Keep this draft private until the owner chooses a license and publication policy.
