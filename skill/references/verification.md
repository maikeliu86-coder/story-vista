# Verification

Run:

```bash
python scripts/storyvista.py validate output/story
python -m unittest discover -s tests -v
```

The validator checks required files, JSON parsing, major-character IDs, relation endpoints, evidence state, unique asset IDs, manifest bindings, placeholder paths, portrait coverage, and the initials-avatar policy.

Browser verification should cover at least desktop and mobile widths. Test navigation, search, filters, evidence drawer, Actor Mode switching, image loading, text overflow, and console errors.
