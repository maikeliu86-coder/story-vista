# Main Demo

The main checked-in demo source is:

- [reader-visual-codex-demo input](../skill/examples/reader-visual-codex-demo/input.txt)
- [reader-visual-codex-demo expected output](../skill/examples/reader-visual-codex-demo/expected/)

Build it locally:

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
python scripts/storyvista.py validate output/reader-visual-codex-demo
```

Open `output/reader-visual-codex-demo/atlas.html`.
