# Data Contracts

Canonical JSON Schemas live in `skill/templates/`:

- `source-index.schema.json`: source identity, path, title, language, and size.
- `chunks.schema.json`: stable chunk IDs, offsets, headings, text, and summaries.
- `story-atlas.schema.json`: metadata, entities, relations, events, timeline, Actor Mode, visual style, and evidence index.
- `visual-asset-plan.schema.json`: required visual intent before rendering.
- `image-manifest.schema.json`: final asset paths, provider, status, binding, alt text, and rights note.

Stable IDs use readable prefixes such as `char_001`, `loc_001`, `rel_001`, and `evt_001`. Relations must reference existing entity IDs. Assets must bind to an existing entity or event. Evidence statuses distinguish source facts from interpretation.
