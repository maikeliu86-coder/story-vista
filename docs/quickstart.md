# Quick Start

Requirements: Python 3.8+ and a browser. No coding agent, package install, API key, or image provider is required.

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
python scripts/storyvista.py validate output/reader-visual-codex-demo
```

Open `output/reader-visual-codex-demo/atlas.html`.

Use `--ui-language en` or `--ui-language zh-CN` to override the detected interface language. Use `--spoiler-mode full` only when the reader explicitly wants later locked material revealed.

The main demo shows character aliases, relationship locks, locations, an interpretive map, a blue luminous potion, a red sonic weapon, object/lore cards, Reader Sync, source highlights, evidence jumps, and semantic SVG fallback.
