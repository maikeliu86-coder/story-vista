# External Image Generation

StoryVista v0.4 supports a complete external generation loop without requiring one image vendor:

```bash
python scripts/storyvista.py build input.txt --out output/demo
python scripts/storyvista.py export-prompts output/demo --provider jimeng
python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated
python scripts/storyvista.py rebuild-atlas output/demo
```

The build creates `prompt-pack.md`, provider-specific files under `prompts/`, expected filenames, placeholder display assets, and manifest records with `pending_external_generation`. After binding, exact filename matches become `generated_external`; accepted fuzzy matches become `user_provided`.

The atlas exposes image status, Copy prompt, Open prompt pack, expected filename, and replacement instructions. Direct API providers remain configurable extension points; no paid generation call is made by the standard-library runtime.
