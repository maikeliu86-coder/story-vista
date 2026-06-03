# Quick Start

## What you need

- Codex with local skills support
- A novel, script, screenplay, RPG setting, story bible, or long-form narrative notes
- Optional: Obsidian, Image2 / GPT-Image, and a static hosting target

## Install

Copy the skill into your Codex skills directory:

```bash
mkdir -p "$HOME/.codex/skills"
cp -R skill "$HOME/.codex/skills/story-vista"
```

Start a new Codex session and invoke:

```text
Use $story-vista to turn this novel, script, or long-form text into an interactive visual atlas for characters, relationships, scenes, locations, timelines, and worldbuilding concepts.
```

## Recommended first run

1. Provide the source text or point Codex to the file.
2. Ask for an entity audit first: characters, places, objects, factions, concepts, and timeline.
3. Review the entity list and correct names or categories.
4. Ask StoryVista to build the first visual atlas.
5. Review image matching, relationship labels, and mobile behavior.

## Recommended atlas request

For the revised skill, ask for a responsive interactive archive rather than a static summary:

```text
Use $story-vista to read this story first, separate characters, places, ships, technologies, powers, organizations, objects, and clues, then build a responsive interactive visual atlas for desktop, tablet, and mobile. Include character cards, a grouped character relationship tree, character profiles, concept/timeline views, and a real 3D space map when spatial relationships matter.
```

If you already have a strong page style to reuse:

```text
Use $story-vista to follow the layout and interaction logic of this existing atlas, but replace all content with the new source text. Keep the corrected responsive, classification, character graph, and true 3D space-map rules.
```

## Review checklist

- Characters are not mixed with places, ships, objects, or organizations.
- Aliases and translations are grouped under the correct entity.
- Relationship labels are evidence-based.
- Scene/location maps match the story order.
- Generated images are reviewed before public use.
- Private manuscripts and local file paths are not published accidentally.
- Character thumbnails preserve aspect ratio and do not cover faces with names.
- Character graphs keep relationship text readable and support clickable avatars.
- Technology, power, weapon, device, and object timelines explain story function.
- 3D space maps use model volume and clickable model bodies, not flat photo cards.
- Desktop, tablet, and mobile layouts are checked before sharing.
