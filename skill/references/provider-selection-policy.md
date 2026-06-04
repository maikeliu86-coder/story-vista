# Default Image Provider Selection Policy

StoryVista uses an automatic provider selection policy by default.

## Default Principles

1. Auto Mode is the default.
2. Do not force beginners to choose from a long provider list.
3. If exactly one verified provider is detected, select it automatically.
4. If multiple verified providers are detected, recommend the highest-scoring provider and explain why.
5. If no verified provider is detected, use `prompt-only` or `placeholder-svg` mode.
6. If the user explicitly configured a provider, respect the user configuration.
7. If the user previously selected a provider, prefer the last selected provider when still available.
8. Always allow manual override.
9. Always explain the selected provider in simple language.
10. Never silently fall back to initials-only avatars.

## Selection Priority

1. Explicit user config in `image-provider.config.yaml`.
2. User selection from current session.
3. Previously saved user preference if available.
4. Verified provider with highest StoryVista fit score.
5. Detected but unverified provider with highest score.
6. Prompt-only provider.
7. Manual assets mode.
8. Semantic `placeholder-svg` mode.
9. Initials-only avatar only if explicitly allowed.

Default: `allow_initials_avatar: false`.

## Provider Scoring

Each detected provider should receive a `score` from 0 to 100 plus `selection_reason` and `risk_reasons`.

Scoring dimensions:

- `callable_api`
- `verified`
- `storyvista_fit`
- `character_consistency`
- `location_keyart_quality`
- `chinese_prompt_support`
- `global_accessibility`
- `local_accessibility`
- `cost_predictability`
- `speed`
- `supports_image_to_image`
- `supports_batch_generation`
- `supports_manual_workflow`
- `user_region_fit`
- `config_clarity`

This is a practical recommendation score, not a universal quality ranking.

## Multiple Providers

When multiple candidates are detected, do not ask beginners to choose. Recommend one:

中文：

检测到多个可能可用的生图引擎。StoryVista 已根据当前环境和故事视觉化需求为你推荐：{selected_provider}。推荐原因：{selection_reason}。你可以继续使用推荐引擎，也可以手动切换。

选项：

- 继续使用推荐引擎
- 查看并切换其他引擎

English:

Multiple image provider candidates were detected. StoryVista recommends {selected_provider} based on your current environment and story visualization needs. Reason: {selection_reason}. You can continue with the recommended provider or switch manually.

Options:

- Continue with recommended provider
- View and switch providers

Default: `ask_when_multiple_verified: false`.

## One Provider

中文：

检测到可用生图引擎：{provider}。StoryVista 将使用它生成或规划人物、地点和关键事件视觉资产。你可以在设置中随时切换。

English:

Detected available image provider: {provider}. StoryVista will use it to generate or plan character, location, and key event visuals. You can switch providers at any time.

Continue automatically unless the provider state is high risk.

## No Provider

中文：

当前没有检测到可直接调用的生图引擎。StoryVista 将使用 Auto Fallback：生成完整图片提示词、image-manifest.json 和语义占位图。你可以之后配置生图引擎并重新生成视觉资产。

English:

No directly callable image provider was detected. StoryVista will use Auto Fallback: full image prompts, image-manifest.json, and semantic placeholders. You can configure an image provider later and regenerate visual assets.

Do not stop. Continue with `prompt-only` or `placeholder-svg`.

## Detected But Unverified

An API key, config file, or endpoint URL is a detection signal, not proof that image generation will work. When no safe verification call has run, StoryVista may still recommend the highest-scoring candidate, but the report must say `verified: false`, include `provider_configured_but_unverified` or `provider_unreachable` in `risk_reasons`, and explain that no test image call was made.

If the selected provider is a prompt-only or manual workflow, report that mode plainly and continue through prompts, manifest entries, manual asset binding, or semantic placeholders.

## Secondary Confirmation

Ask only for high-risk states:

- `no_provider_detected`
- `provider_configured_but_unverified`
- `provider_unreachable`
- `placeholder_only`
- `prompt_only`
- `allow_initials_avatar` is true
- user selected a provider with unknown capability
- image generation is disabled
- current provider does not support image generation
- selected provider requires manual generation outside the agent

Chinese:

当前配置可能无法直接生成完整图片资产，StoryVista 将使用 prompt-only 或 semantic placeholder 模式继续。是否继续使用当前设置？

Options:

- 是，继续使用当前设置
- 否，查看推荐生图引擎

English:

The current configuration may not be able to generate complete image assets directly. StoryVista will continue in prompt-only or semantic placeholder mode. Continue with the current settings?

Options:

- Yes, continue with current settings
- No, show recommended image providers

If the user continues, record `user_confirmed_current_provider: true`.
