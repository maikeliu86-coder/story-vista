# Visual Atlas Demo

This demo is a public, original Chinese prose sample for StoryVista Raw Narrative Mode. It is written like a short fiction fragment instead of using structured directives, so it exercises the normal story-reading path.

## What This Demo Shows

The demo shows how StoryVista can turn prose into a visual reading atlas:

- Characters with evidence-aware profiles
- Relationships and faction tension
- Locations and spatial structure
- Objects, lore, and visual codex entries
- Events and spoiler-safe source evidence
- Image prompts and semantic fallback assets

## Run The Demo

From the repository root:

```bash
python3 scripts/storyvista.py build examples/visual-atlas-demo/story.md --out output/visual-atlas-demo
python3 scripts/storyvista.py validate output/visual-atlas-demo
```

Open:

```text
output/visual-atlas-demo/atlas.html
```

`output/` is generated locally and should not be committed.

## Expected Output

The build should create:

- `story-atlas.json`
- `character-atlas.json`
- `relationship-web.json`
- `location-atlas.json`
- `object-lore-codex.json`
- `visual-asset-plan.json`
- `image-manifest.json`
- `prompt-pack.md`
- `manual-generation-instructions.md`
- `atlas.html`
- semantic fallback assets under `assets/`

## Why It Is Useful For Raw Narrative Mode

This story includes named characters, unnamed characters, organizations, places, artifacts, faction language, ambiguous loyalties, and multiple event beats. That makes it a good regression sample for checking whether StoryVista extracts story entities from prose without relying on `Character:`, `Location:`, or other directive formats.

## Pages To Inspect

- **Characters**: confirm named and unnamed people are separated from objects, actions, and atmospheric nouns.
- **Relationships**: confirm links are based on real character or faction interaction.
- **Locations**: confirm places are extracted without turning every door or corridor into a major location.
- **Objects & Lore**: confirm artifacts such as the compass, chip, umbrella, map, badge, and memory box are captured.
- **Maps**: confirm the station, pier, archive, and central system form a readable spatial structure.
- **Reader / source evidence**: confirm claims can be traced back to story text without revealing later plot.

## Companion Files

- `expected-output.md`: human golden reference for extraction quality.
- `image-prompts.md`: prompt pack for manually generating demo visuals.
- `demo-notes.md`: design intent and known limits.
