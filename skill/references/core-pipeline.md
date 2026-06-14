# Core Pipeline

`scripts/storyvista.py build <input> --out <directory>` runs the complete v0.2 pipeline:

1. `ingest_source` records the source and language.
2. `chunk_text` creates stable source chunks and offsets.
3. `extract_entities` builds the story model and evidence layer.
4. `build_visual_asset_plan` creates required character, location, and event assets.
5. `build_image_manifest` binds every asset to an entity or event.
6. `generate_placeholders` writes local semantic SVGs.
7. `render_atlas` embeds data in the static HTML template.
8. `validate_output` writes the verification report.

The minimal implementation is deterministic, local, and standard-library only. Provider calls, advanced NLP, graph layout, and 3D scenes belong in optional adapters, not the core build.
