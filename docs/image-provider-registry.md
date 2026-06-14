# Image Provider Registry

`skill/templates/provider-registry.json` is the portable StoryVista provider catalog. Each entry records region, provider type, capabilities, configuration signals, prompt export support, manual binding support, and generation availability.

The registry separates similarly branded routes when their operating model differs. `jimeng` and `jianying-jimeng` are manual web workflows. `bytedance-seedream` is a configurable integration target, while `volcengine-seedream` represents the Volcengine API route. Detection means configuration is present, not that an account, endpoint, quota, or paid call has been verified.

Provider groups include direct APIs, local APIs, agent-native tools, manual web tools, prompt-only tools, manual assets, and fallbacks. StoryVista never installs a provider or creates a paid account automatically.
