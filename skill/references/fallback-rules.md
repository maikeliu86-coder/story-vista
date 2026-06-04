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

## Semantic Placeholder Standard

Semantic placeholders should include:

- full canonical name
- entity type
- asset type
- stable asset id
- readable visual category

They should be clear temporary stand-ins, not fake final images.
