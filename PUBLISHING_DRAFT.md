# Publishing Draft Notes

This repository is a draft package for internal confirmation.

## Current Status

- GitHub hero image generated with Image2 and stored at `assets/github-hero.png`.
- English and Chinese README files are prepared.
- The installable skill is stored under `skill/`.
- No public release should be created until the owner confirms.

## Recommended GitHub Flow

1. Create a private GitHub repository named `story-interactive-archive`.
2. Push this draft to a branch named `draft/internal-review`.
3. Open a draft pull request into `main`.
4. Review README text, hero image, and skill behavior.
5. Only after approval, merge and optionally make the repository public.

## Validation

Run:

```bash
python3 /Users/wangzhipeng/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill
```
