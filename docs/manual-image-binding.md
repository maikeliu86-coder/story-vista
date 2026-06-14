# Manual Image Binding

Generate or collect PNG, JPG, JPEG, or WEBP files and name them using the expected filenames shown in the atlas or prompt pack. Then run:

```bash
python scripts/storyvista.py bind-images output/demo --assets path/to/generated-images
```

StoryVista first tries exact asset-ID filename matching, then a conservative fuzzy match. Matched files are copied to `assets/generated/`, `image-manifest.json` is updated, `binding-report.json` records the decision, and `atlas.html` is rebuilt automatically. Unmatched files are reported and left untouched.
