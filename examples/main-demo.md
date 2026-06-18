# Main Demo

This demo shows the kind of story material StoryVista should turn into a visual atlas. The finished atlas should feel like a game codex, worldbuilding archive, or film concept dossier before it feels like a workflow report.

The current product experience reference is documented in:

- [Golden Reference](../docs/golden-reference.md)
- [Product Experience Contract](../docs/product-experience-contract.md)

The Markdown below is not the target user experience. It is a source checklist for what the rendered atlas should visualize with cards, relationship surfaces, timelines, maps, and prompt-ready image slots.

## Raw Narrative Mode Example

StoryVista should also work when the user gives ordinary prose without labels. For example:

```text
雨水从渡口客栈的檐角落下，林砚推开木门时，柜台后的油灯已经快灭了。苏晚正把一块青铜令牌藏进袖中，她说这东西不是陆家的货，而是青鸦帮昨夜从北仓抢来的凭证。

黑衣人撞开后窗，几名捕快挤进客栈。王捕头命令众人放下刀，又盯着苏晚袖口的暗纹，问她是不是替青鸦帮送信。林砚把掌柜护到柱后，听见后巷传来马蹄声。

老者从灶房里走出来，递给林砚一封密信。信上写着雾桥码头三更换船。苏晚低声说，如果王捕头真的效忠巡检司，就该先查青鸦帮，而不是抓她。
```

Expected atlas behavior:

- Characters: named people such as 林砚、苏晚、王捕头, plus unnamed figures such as 黑衣人 A、捕快 A、老者 A.
- Locations: 渡口客栈、北仓、后巷、雾桥码头.
- Objects and lore: 青铜令牌、密信、刀 or short weapon cues when present.
- Organizations: 青鸦帮、巡检司、陆家 when the text supports them.
- Events and relationships: arrival, confrontation, delivery, protection, pursuit, and suspicion should become timeline and relationship-web entries.
- Spoiler safety: only facts inside the pasted prose are visible; suspected motives remain unresolved.
- Image workflow: if no callable image provider is available, the atlas should keep the immersive semantic fallback cards and export prompt task rows instead of blank images.

## Source Excerpt

```text
Chapter 3: The Glass Meridian

Elara Voss reached Northreach Observatory before dawn, carrying the brass astrolabe wrapped in her father's blue scarf. The city below was still dark, except for the signal lamps of the Meridian Guild blinking along the cliff road.

Kael Durn waited beside the cracked star map. He had once served the Guild as a courier, but now every guard in Northreach knew his face from the wanted posters. "The astrolabe does not point north," he said. "It points to the door under the harbor."

Master Orlon, keeper of the Observatory, refused to touch the device. He told Elara that the last scholar who opened the harbor door vanished before the winter flood. Mira Hale, a mapmaker from the Free Coast, marked three routes on the table: the cliff road, the old aqueduct, and the tide tunnel.

When the Guild bell rang, Captain Thorne entered with six lantern guards. He did not arrest Elara. Instead, he ordered everyone to surrender the astrolabe to the Council before sunset.

Elara noticed the red wax seal on Thorne's order. It was not the Guild seal. It belonged to the Ash Regent.
```

## People

| Character | Role | Faction | Current Evidence |
|---|---|---|---|
| Elara Voss | protagonist / carrier of the astrolabe | independent, possibly family-linked to the artifact | Carries the brass astrolabe and notices the false seal. |
| Kael Durn | wanted former courier | ex-Meridian Guild | Knows the astrolabe points to a harbor door and is wanted by city guards. |
| Master Orlon | observatory keeper | Northreach Observatory | Warns about the scholar who vanished after opening the harbor door. |
| Mira Hale | mapmaker | Free Coast | Marks three possible routes to the harbor door. |
| Captain Thorne | lantern guard captain | official guard force, possibly compromised | Orders surrender of the astrolabe using a document sealed by the Ash Regent. |
| Ash Regent | unseen political force | unknown / external power | The red wax seal on Thorne's order belongs to the Regent. |

## Relationships

| Source | Target | Relationship | Spoiler State | Evidence |
|---|---|---|---|---|
| Elara Voss | Kael Durn | uneasy ally | visible | They meet before dawn and discuss the astrolabe. |
| Kael Durn | Meridian Guild | former courier / fugitive | visible | He once served the Guild and is now wanted. |
| Master Orlon | Northreach Observatory | keeper | visible | He is named as keeper of the Observatory. |
| Captain Thorne | Elara Voss | authority pressure | visible | He orders surrender of the astrolabe but does not arrest her. |
| Captain Thorne | Ash Regent | suspicious indirect link | visible but unresolved | His order carries the Ash Regent's seal. |

## Locations

| Location | Type | Story Function | Evidence |
|---|---|---|---|
| Northreach Observatory | observatory / high landmark | meeting point and knowledge archive | Elara reaches it before dawn. |
| Northreach city | city below the cliff | political and guard pressure | Guards know Kael's face. |
| Cliff road | route | visible route to/from the observatory | Signal lamps blink along it. |
| Harbor door | hidden place | central mystery destination | Kael says the astrolabe points to it. |
| Old aqueduct | route | possible approach | Mira marks it as a route. |
| Tide tunnel | route | risky hidden approach | Mira marks it as a route. |

## Objects And Lore

| Object / Concept | Type | Meaning | Evidence |
|---|---|---|---|
| Brass astrolabe | artifact | points to a hidden harbor door, not north | Elara carries it; Kael explains its direction. |
| Blue scarf | personal object | family memory or protection marker | The astrolabe is wrapped in her father's scarf. |
| Cracked star map | observatory object | planning surface and knowledge artifact | Kael waits beside it. |
| Red wax seal | political clue | links Thorne's order to the Ash Regent | Elara identifies the seal. |
| Meridian Guild signal lamps | worldbuilding system | organized city communication network | Lamps blink along the cliff road. |

## Factions

| Faction | Known Role | Current Status |
|---|---|---|
| Meridian Guild | city institution tied to couriers, lamps, and council orders | visible but possibly infiltrated |
| Free Coast | Mira's origin or affiliation | visible, not yet explained |
| Lantern guards | armed city authority | visible |
| Ash Regent | external or hidden power | unresolved threat |

## Timeline

| Order | Event | Spoiler State |
|---|---|---|
| 1 | Elara arrives at Northreach Observatory before dawn with the astrolabe. | visible |
| 2 | Kael explains that the astrolabe points to the harbor door. | visible |
| 3 | Orlon warns that a previous scholar vanished after opening the door. | visible |
| 4 | Mira marks three possible routes. | visible |
| 5 | Thorne arrives and orders surrender of the astrolabe. | visible |
| 6 | Elara notices the order uses the Ash Regent's seal. | visible but unresolved |

## Spoiler-Safe Notes

- The atlas should not explain what is behind the harbor door unless that appears within the current reading scope.
- The Ash Regent's motive should remain unresolved.
- Thorne should be marked suspicious, not confirmed as a traitor.
- The vanished scholar should remain a mystery, not a solved backstory.

## Image Generation Task List Example

| ID | Type | Title | Source Basis | Prompt | Negative Prompt | Recommended Provider | Aspect Ratio | Priority |
|---|---|---|---|---|---|---|---|---|
| image_001 | character | Elara Voss portrait | Elara carries the brass astrolabe wrapped in her father's blue scarf. | Portrait of a young determined scholar-traveler at dawn, holding a brass astrolabe wrapped in a blue scarf, cliffside observatory light, cinematic but evidence-strict, no future plot details. | spoilers, extra characters, modern clothing, readable text, watermark, unrelated symbols | Image2 / SeeDream / Flux | 4:5 | high |
| image_002 | location | Northreach Observatory | Elara reaches the observatory before dawn; city below is dark. | Cliffside stone observatory before dawn above a dark harbor city, signal lamps on the cliff road, cold blue light, grounded fantasy realism, no characters. | battle scene, futuristic city, unread plot symbols, text, watermark | SeeDream / SDXL / Flux | 16:9 | high |
| image_003 | object | Brass astrolabe | The astrolabe points to the harbor door instead of north. | Close-up brass astrolabe wrapped in a worn blue scarf on a cracked star map, candlelit observatory table, mysterious but spoiler-safe. | glowing portal, revealed harbor door interior, text labels, watermark | Image2 / ComfyUI / SDXL | 1:1 | medium |

## Local Build Reference

The checked-in full demo source remains available at:

- [reader-visual-codex-demo input](../skill/examples/reader-visual-codex-demo/input.txt)
- [reader-visual-codex-demo expected output](../skill/examples/reader-visual-codex-demo/expected/)

Build it locally:

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
python scripts/storyvista.py validate output/reader-visual-codex-demo
```

Open `output/reader-visual-codex-demo/atlas.html`.
