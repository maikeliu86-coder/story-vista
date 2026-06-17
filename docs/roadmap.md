# Roadmap

This roadmap describes the intended public evolution of StoryVista from a stable core Skill to a broadly usable visual reading workflow.

## v0.1 - 基础 Skill 稳定化

### Goal

Make the core StoryVista workflow reliable for local use.

### Deliverables

- stable Python CLI commands
- deterministic source indexing and chunking
- character, location, object, and relationship extraction
- spoiler-aware data handling
- output atlas generation
- validation command and basic test coverage

## v0.2 - 多 Agent 兼容

### Goal

Make StoryVista usable across coding agents instead of coupling it to one assistant runtime.

### Deliverables

- Codex usage path
- Claude Code usage path
- Cursor and Trae compatibility guidance
- generic agent usage rules
- stable file-based interface instead of hidden runtime assumptions

## v0.3 - 多图像模型 provider workflow

### Goal

Separate StoryVista's reading workflow from any single image generation engine.

### Deliverables

- provider-neutral prompt export
- provider preflight checks
- provider recommendation logic
- manual image binding workflow
- support docs for Image2, SeeDream, ComfyUI, Flux, and SDXL

## v0.4 - Demo 与可视化样例

### Goal

Show real examples of how StoryVista looks and how the workflow behaves in practice.

### Deliverables

- curated demo inputs
- sample atlases
- README hero and workflow imagery
- public-facing examples for English and Chinese reading flows
- provider workflow examples with binding-ready outputs

## v0.5 - Web Demo / GitHub Pages / Vercel

### Goal

Make StoryVista easier to inspect publicly without cloning the repository first.

### Deliverables

- hosted web demo
- GitHub Pages or Vercel deployment path
- static demo outputs
- public navigation for docs and examples
- shareable product-style landing surface for the open-source repo

## v1.0 - 稳定公开版本

### Goal

Ship a stable public version that readers and agent users can adopt without guesswork.

### Deliverables

- stable documentation system
- stable output contract
- verified end-to-end examples
- stronger troubleshooting guidance
- release discipline and migration notes
- public positioning as a spoiler-safe visual reading companion
