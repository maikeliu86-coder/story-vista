# External Image Generation Instructions

1. Choose a provider prompt file under `prompts/`.
2. Generate each image using its expected filename.
3. Save PNG, JPG, JPEG, or WEBP files in `assets/generated/`.
4. Run `python scripts/storyvista.py bind-images OUTPUT --assets OUTPUT/assets/generated`.
5. Run `python scripts/storyvista.py rebuild-atlas OUTPUT` if needed.

Do not upload private manuscripts to an external provider without checking its privacy terms.
