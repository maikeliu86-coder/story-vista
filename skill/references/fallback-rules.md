# Fallback Rules

Use this order:

1. User-provided licensed asset.
2. Generated asset from the configured provider.
3. Provider-ready prompt.
4. Generic prompt.
5. Semantic SVG with full name, entity type, and visual category.
6. Initials-only avatar only after explicit user opt-in.

Every fallback must be visible in `image-manifest.json`. Missing providers never block text parsing or atlas generation.
