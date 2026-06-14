# v0.4 Upgrade Report

StoryVista v0.4 adds the Real Image Provider Layer while preserving a provider-neutral core.

- A portable provider registry covers direct APIs, local tools, manual web tools, prompt-only routes, manual assets, and fallbacks.
- Jimeng, Jianying Jimeng, ByteDance Seedream, and Volcengine Seedream are distinct provider entries.
- Every build exports a provider-neutral prompt pack, provider-specific prompts, generation instructions, expected filenames, and binding-ready manifest records.
- External images can be scanned, matched, copied, registered, and displayed through the CLI.
- The atlas explains pending generation and exposes prompt actions instead of silently presenting placeholders as final art.

The standard runtime does not make paid provider calls. Direct adapters remain configurable extension points that require user credentials and explicit setup.
