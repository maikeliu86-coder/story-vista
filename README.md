# StoryVista

![StoryVista hero](assets/github-hero.png)

**StoryVista** helps people make text worlds visible.

Turn novels, scripts, screenplays, and long-form text into interactive visual atlases for characters, scenes, timelines, concepts, and worlds.

Chinese name: **文景**  
Tagline: **Make Text Worlds Visible** / **让文字世界看得见**

> Draft status: this repository is prepared for internal review. Do not publish, release, or make public until the owner confirms the content and presentation.

## Reading a story should not feel like losing a map

Long stories often hide their structure inside names, places, scenes, and scattered clues. StoryVista makes that hidden structure visible.

![Reading pain points overview](assets/pain-points-overview.png)

## Visual Pain Points

|  |  |
| --- | --- |
| ![Name Overload](assets/pain-name-overload.png)<br><br>**Name Overload**<br>Too many characters, aliases, translations, titles, and nicknames make it hard to remember who is who.<br><br>**人物名字混乱**<br>人物、别名、译名、头衔和昵称太多，读到后面很容易分不清谁是谁。 | ![Relationship Confusion](assets/pain-relationship-confusion.png)<br><br>**Relationship Confusion**<br>Allies, enemies, families, mentors, rivals, and hidden identities shift across the story.<br><br>**人物关系混乱**<br>同盟、敌对、亲属、导师、竞争者和隐藏身份不断变化，关系线越读越乱。 |
| ![Place Disorientation](assets/pain-place-disorientation.png)<br><br>**Place Disorientation**<br>Scenes move between cities, rooms, planets, kingdoms, or timelines before the reader forms a mental map.<br><br>**地点描述混乱**<br>故事在城市、房间、星球、王国或时代之间跳转，读者还没形成地图，场景已经切走。 | ![Spatial Uncertainty](assets/pain-spatial-uncertainty.png)<br><br>**Spatial Uncertainty**<br>Routes, distances, worlds, ships, battlefields, or fantasy realms are described in text but hard to visualize.<br><br>**空间关系混乱**<br>路线、距离、世界、飞船、战场或幻想地理只存在于文字里，很难形成直观空间感。 |

## From Text to Visual Atlas

StoryVista turns narrative material into an explorable structure that readers and creative teams can revisit at a glance.

- **Character Graphs｜人物关系图**  
  Map names, aliases, roles, factions, and changing relationships.

- **Scene & Location Maps｜场景与地点地图**  
  Connect rooms, cities, planets, kingdoms, routes, and recurring places.

- **Timelines & Concepts｜时间线与概念卡片**  
  Track plot events, technologies, powers, motifs, objects, and clues.

- **3D World Maps｜3D 世界图谱**  
  Build interactive spatial views when distance, geography, or movement matters.

![StoryVista workflow](assets/storyvista-workflow.png)

## Built for people who think through stories

- Readers who want to remember complex stories
- Writers who want to test story structure
- Screenwriters who track scenes and characters
- Students and teachers analyzing literature
- Worldbuilders managing places, factions, and lore
- Researchers turning narrative material into navigable knowledge

## What It Helps Build

- Interactive character relationship trees
- Character or role indexes with portraits and summaries
- Scene, location, object, faction, and world maps
- Plot, technology, power, or motif timelines
- Image2 / GPT-Image visual assets matched one-to-one to story entities
- Mobile-friendly archive pages for readers and collaborators
- Obsidian-ready local pages plus optional public static sharing
- Real-time 3D maps for spatial stories, journeys, planets, cities, rooms, or worlds

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
│   ├── github-hero.png
│   ├── pain-points-overview.png
│   ├── pain-name-overload.png
│   ├── pain-relationship-confusion.png
│   ├── pain-place-disorientation.png
│   ├── pain-spatial-uncertainty.png
│   └── storyvista-workflow.png
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

- [ ] The visual pain-point section is clear across cultures.
- [ ] The English README explains the skill within the first screen.
- [ ] The Chinese README speaks to readers, writers, screenwriters, and worldbuilders.
- [ ] The new images fit the GitHub details page.
- [ ] `skill/SKILL.md` describes trigger conditions clearly.
- [ ] `skill/references/implementation-notes.md` captures reusable workflow details.
- [ ] The skill validates with `quick_validate.py`.
- [ ] The repository remains unpushed until the owner approves publication.

## License

No public license is assigned yet. Keep this draft private until the owner chooses a license and publication policy.
