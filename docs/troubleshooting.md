# Troubleshooting

## I only see placeholders

This means no real image has been bound yet. Open `prompt-pack.md`, generate images with your chosen provider, save them with the expected filenames, then run:

```bash
python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated
```

## Provider keys are detected but images are not generated

Provider preflight records configuration signals only. A detected key is not a verified callable runtime. Review [Provider Workflow](provider-workflow.md) and [Visual Provider Preflight](visual-provider-preflight.md).

## The atlas does not open correctly

Run validation first:

```bash
python scripts/storyvista.py validate output/demo
```

Then check that `atlas.html`, `story-atlas.json`, `image-manifest.json`, `prompt-pack.md`, and `manual-generation-instructions.md` exist in the output directory.
