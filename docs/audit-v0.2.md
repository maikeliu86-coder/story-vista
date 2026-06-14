# StoryVista v0.2 Repository Audit

Audit date: 2026-06-15

## Executive Finding

StoryVista has a strong product idea, useful cross-agent guidance, image-provider design notes, schemas, and bilingual positioning. Before v0.2, however, it is primarily a documentation package: there is no runnable `storyvista.py` build command, no source/chunk/evidence pipeline, no HTML renderer, and no automated verification of a complete output folder.

The v0.2 priority is therefore subtraction and closure: one dependency-free CLI, one fictional demo, one placeholder-first visual pipeline, one evidence-aware Story Atlas contract, one Actor Mode prototype, and one verification report.

## 1. Current Structure

- Root documentation: README files, AGENTS.md, llms.txt, changelog, contribution and security files.
- `skill/`: a 396-line Skill document, agent notes, references, templates, and documentation-only examples.
- `scripts/`: image-provider detection scripts only.
- `docs/`: product, promotion, release, prompt, and roadmap notes.
- `assets/`: README illustrations, but no screenshot of a generated atlas.
- Missing before v0.2: runnable builder, package modules, HTML template, source/chunk schemas, evidence-aware data model, tests, and generated demo output.

## 2. Repeated Documentation

Image-provider behavior is repeated across README, README.zh-CN, AGENTS.md, llms.txt, SKILL.md, and seven reference files. The same concepts recur: preflight, detection, selection, fallback, switching, recommendations, and asset planning.

Recommended correction: make `skill/references/image-provider.md` canonical; keep old files as compatibility pointers or narrowly scoped historical notes.

## 3. Missing Critical Files

- `scripts/storyvista.py`
- `src/storyvista/` pipeline modules
- `skill/templates/source-index.schema.json`
- `skill/templates/chunks.schema.json`
- `skill/templates/visual-asset-plan.schema.json`
- `skill/templates/atlas.html`
- `tests/` covering build, relations, evidence, placeholders, and schemas
- `docs/design-system.md`, `docs/legal-and-rights.md`, `docs/product-vision.md`
- a real demo `input.txt` and expected output

## 4. README Commands

The previous README described installation and provider diagnosis, but did not provide a command that built an atlas from source text. The v0.2 README must only advertise commands verified in this repository.

## 5. Schema Status

`story-atlas.schema.json` and `image-manifest.schema.json` exist, but they describe the earlier provider-heavy model. They do not fully encode the requested v0.2 evidence index, Actor Mode, source chunks, or simplified binding contract. Source-index, chunks, and visual-asset-plan schemas are missing.

## 6. Example Status

The minimal example contains prose plus hand-authored image planning files. It cannot be rebuilt from a command and does not demonstrate source indexing, evidence, Actor Mode, HTML rendering, or verification.

## 7. Script Status

The provider detectors are runnable and safety-minded, but they do not build a Story Atlas. Their role should become optional plugin diagnosis rather than the main workflow.

## 8. Provider Documentation

Provider documentation is the most developed subsystem and the most duplicated. It currently occupies more attention than ingest, entity modeling, evidence, rendering, and validation combined.

## 9. Skill Execution Length

The previous `skill/SKILL.md` is 396 lines with an 18-step provider-aware workflow. It is too long for a hard execution contract. v0.2 should use a six-step pipeline and move details to references.

## 10. Minimum Closed Loop

Before this upgrade, the required loop did not exist:

`input.txt -> source-index.json -> chunks.json -> story-atlas.json -> visual-asset-plan.json -> image-manifest.json -> placeholders -> atlas.html -> verification-report.md`

## 11. UI And Demo Evidence

The repository has conceptual README graphics but no screenshot or mockup of the generated product. It does not yet show Actor Mode, evidence tags, relationship exploration, or a visual bible.

## v0.2 Decision

Implement one conservative, standard-library pipeline. Prefer explicit metadata and evidence-backed heuristics over impressive but unsupported extraction. Generate semantic SVG placeholders by default. Make Reader Mode and Actor Mode usable in a cinematic static atlas. Treat all API image providers and agent runtimes as optional interfaces unless directly implemented and tested.
