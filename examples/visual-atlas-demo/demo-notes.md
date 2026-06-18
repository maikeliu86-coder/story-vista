# Demo Notes

## Design Intent

This demo is designed to show StoryVista as a visual reading atlas, not as an engineering report. The story uses a compact science-fiction mystery with a station, sealed archive, ambiguous ally, secret organizations, and visually distinct artifacts. Those ingredients should produce useful Characters, Relationships, Locations, Objects & Lore, Maps, and Reader evidence pages.

## Why This Story Topic

The abandoned station and hidden archive setup naturally creates visual surfaces:

- Character portraits with faction tension
- Dark station and underground route key art
- Artifact cards for the compass, umbrella, chip, lamp, map, badge, and memory box
- A relationship network between former partners, missing family, institutions, and secret groups
- A spatial map linking station, pier, archive, and hidden central system

The story is original and suitable for public repository use. It avoids real people, existing franchises, and copyrighted settings.

## Capabilities Tested

- Raw Narrative Mode without directive syntax
- Chinese character name extraction
- Unnamed character handling
- Organization detection
- Location extraction without over-promoting every object or doorway
- Object and lore extraction
- Event segmentation across multiple plot beats
- Relationship extraction under ambiguity
- Evidence links back to prose
- Visual asset planning and semantic fallback generation

## Visual Reading Atlas Criteria

The finished atlas should feel like an interactive story world reference:

- Characters should be browseable as dossier entries.
- Relationships should feel like a network of people and factions.
- Locations should suggest a coherent geography.
- Objects and lore should feel like codex cards.
- Source evidence should support claims without taking over the main visual experience.

## Known Limits

- This is a short prose sample, not a full novel.
- Some entities can reasonably belong to multiple categories. For example, `镜海中枢` can be a location, lore concept, or both.
- The extractor may choose different boundaries for unnamed characters.
- Generated image quality depends on the external provider and prompt interpretation.
- The demo does not include committed generated images; it only includes prompts and expected outputs.

## Binding Real Images Later

1. Build the demo:

   ```bash
   python3 scripts/storyvista.py build examples/visual-atlas-demo/story.md --out output/visual-atlas-demo
   ```

2. Use `output/visual-atlas-demo/prompt-pack.md` or this demo's `image-prompts.md` to generate images externally.

3. Save images using the expected filenames shown by StoryVista.

4. Bind images:

   ```bash
   python3 scripts/storyvista.py bind-images output/visual-atlas-demo --assets output/visual-atlas-demo/assets/generated
   ```

5. Reopen `output/visual-atlas-demo/atlas.html`.

Do not commit `output/` or generated test assets unless a future release intentionally adds curated demo images under a reviewed examples asset folder.
