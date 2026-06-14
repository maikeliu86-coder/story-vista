# Image Provider

StoryVista is provider-neutral. The provider changes visual asset production, not story extraction or the data model.

## Capability Levels

- **Level 0 - Placeholder**: no provider. Build prompts, manifest entries, and semantic SVGs.
- **Level 1 - Manual**: user generates or supplies files, then updates `file_path`, `provider`, `status`, and rights notes in `image-manifest.json`.
- **Level 2 - Callable**: an installed API or local engine generates assets from `visual-asset-plan.json`.

## Detection

Run `python scripts/detect_image_provider.py --no-network` for configuration-only checks. Network verification must be explicit and should avoid paid generation calls. Secrets must be masked.

For ComfyUI, inspect environment variables and `.env`, then try a configured endpoint or the local default `http://127.0.0.1:8188`. Safe reachability checks may use `/system_stats` and `/object_info`.

## Switching

1. Keep `story-atlas.json` unchanged.
2. Choose a provider or manual asset folder.
3. Generate assets from `visual-asset-plan.json`.
4. Update `image-manifest.json` paths, provider, status, alt text, and license note.
5. Re-run `scripts/storyvista_build_atlas.py <output>` and validation.

## Recommendations

- Mainland-accessible workflows: local ComfyUI/Stable Diffusion/FLUX, Qwen Image, Hunyuan Image, Wenxin Image, MiniMax, or another service the user can legally access.
- Globally accessible workflows: OpenAI image models, Google image models, Midjourney, FLUX/Stability, Ideogram, Leonardo, Fal, Replicate, or local ComfyUI.

Recommendations are options, not automatic installations. Users remain responsible for account setup, model terms, cost, and content rights.
