# Provider Workflow

StoryVista is provider-neutral. It creates a visual asset plan, prompt pack, provider-specific prompt files, semantic display fallbacks, and an image manifest that can later bind externally generated images.

## Common Flow

```bash
python scripts/storyvista.py build input.txt --out output/demo
python scripts/storyvista.py export-prompts output/demo --provider jimeng
python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated
python scripts/storyvista.py rebuild-atlas output/demo
```

## Related Docs

- [External Image Generation](external-image-generation.md)
- [Image Provider Registry](image-provider-registry.md)
- [Jimeng And Seedream Workflow](jimeng-seedream-workflow.md)
- [Manual Image Binding](manual-image-binding.md)
- [Prompt Pack](prompt-pack.md)
