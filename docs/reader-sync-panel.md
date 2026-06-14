# Reader Sync Panel

`reader-text.json` stores stable paragraph IDs, chapters, offsets, text, and chunk bindings. `entity-linking.json` stores matched ranges, entity IDs, types, confidence, and ambiguity.

Desktop behavior:

- right-side panel
- drag handle for width
- collapse rail
- paragraph search
- persisted open state, width, font size, line height, and progress

Mobile behavior uses a full-screen reader drawer. Clicking highlighted source text opens the related codex section and card. Clicking an evidence button opens the reader and scrolls to the bound paragraph. Temporary focus styling makes both directions visible.
