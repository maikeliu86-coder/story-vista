# Jimeng And Seedream Workflow

## Jimeng / 即梦

Run `python scripts/storyvista.py export-prompts output/demo --provider jimeng`, then open `prompts/jimeng-prompts.md`. Generate each image in Jimeng using the Chinese copy-ready prompt, preserve the requested aspect ratio, and download it using the listed expected filename.

## Seedream / SeeDream

Run `python scripts/storyvista.py export-prompts output/demo --provider seedream`, then use `prompts/seedream-prompts.md` with ByteDance Seedream or Volcengine Seedream. The registry keeps the ByteDance integration target and Volcengine API route separate because setup and credentials may differ.

For either workflow, place generated files in `assets/generated/` and run `bind-images`. Review inferred visual details and provider privacy terms before uploading source-derived material.
