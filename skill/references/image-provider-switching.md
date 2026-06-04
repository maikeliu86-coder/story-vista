# Image Provider Switching

Users can switch providers at any time. Keep `image-manifest.json` as the stable binding layer so character cards, location cards, relationship graph nodes, timelines, and 3D map nodes do not break.

## Switch With Config

Create or edit `image-provider.config.yaml`.

```yaml
image_provider:
  mode: "api"
  provider: "openai"
  model: "gpt-image-2"
  output_folder: "assets/images"
  fallback: "placeholder-svg"
  allow_initials_avatar: false
```

```yaml
image_provider:
  mode: "api"
  provider: "qwen-image"
  model: "user-defined"
  output_folder: "assets/images"
  fallback: "placeholder-svg"
  allow_initials_avatar: false
```

## Switch With Environment Variables

Set only the key needed by the selected provider, such as `OPENAI_API_KEY`, `DASHSCOPE_API_KEY`, `BFL_API_KEY`, or `STABILITY_API_KEY`. StoryVista detection should report `detected` with a masked key and should not print the full value.

## Manual Assets

```yaml
image_provider:
  mode: "manual-assets"
  provider: "local-folder"
  assets_dir: "assets/user-images"
  manifest_path: "image-manifest.json"
  fallback: "placeholder-svg"
  allow_initials_avatar: false
```

Register each supplied image in `image-manifest.json` with `status: "user_provided"`.

## Prompt-Only Mode

```yaml
image_provider:
  mode: "prompt-only"
  provider: "midjourney"
  output_prompt_pack: "storyvista-image-prompts.md"
  fallback: "placeholder-svg"
  allow_initials_avatar: false
```

Use prompt-only mode when the provider is useful but not directly callable by the current agent.

## Placeholder Mode

Use `placeholder-svg` when no provider or manual assets are available. Semantic placeholders must include full entity name and entity type.

## Migrate Between Providers

1. Keep stable `entity_id` and `asset_id` values.
2. Update provider, model, prompt variant, filename, and status in `image-manifest.json`.
3. Regenerate only the visual assets that need replacement.
4. Keep existing user-provided assets unless the user asks to replace them.
5. Re-run atlas binding so UI nodes point to manifest asset ids, not ad hoc paths.

## Regenerate Manifest

When switching providers, regenerate or update `image-manifest.json` from the visual asset plan. Do not delete existing `user_provided` entries unless the user explicitly asks.
