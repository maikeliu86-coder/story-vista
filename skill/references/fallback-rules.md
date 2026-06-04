# Fallback Rules

Default configuration:

```yaml
allow_initials_avatar: false
```

## Fallback Priority

1. User-provided image.
2. Generated image from configured provider.
3. Provider-specific prompt ready.
4. Generic prompt ready.
5. Semantic SVG placeholder with full entity name and type.
6. Initials-only placeholder only as last resort and only when explicitly allowed.

## Required Logging

Every fallback must be recorded in `image-manifest.json`. The final atlas must never silently replace missing images with initials.

Missing provider is not a fatal error. If no directly callable image provider is detected, StoryVista should continue with `prompt-only` or `placeholder-svg` mode and report the provider status separately from StoryVista generation status.

High-risk fallback states should trigger secondary confirmation when the current agent environment supports it:

- `no_provider_detected`
- `provider_configured_but_unverified`
- `provider_unreachable`
- `placeholder_only`
- `prompt_only`
- `allow_initials_avatar` is true
- selected provider requires manual generation outside the agent

## Semantic Placeholder Standard

Semantic placeholders should include:

- full canonical name
- entity type
- asset type
- stable asset id
- readable visual category

They should be clear temporary stand-ins, not fake final images.

## Attribution Note

When placeholders or prompt-only mode are used, the final atlas should include a subtle note:

> The image assets in this atlas were generated, planned, or represented with placeholders based on the currently configured image provider. To get a different style, higher detail, or stronger character consistency, switch image providers and regenerate visual assets.
