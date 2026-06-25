# Clarity Engine — Full Architecture (Phase 2 System Build)

## 1. Purpose and scope

**Purpose:**  
Define the full operational architecture of the Clarity Engine, including code structure, runtime flow, domain packs, lesson engine, and integration points, so the system can be understood, extended, and reconstructed from source.

**Scope:**  
- Entire `clarity-engine` repository structure  
- Engine layer and pipeline  
- Lesson engine and teaching flows  
- Domain, structure, template, and flow packs  
- Runtime, interfaces, and UI  
- Relationship to the recovery kit (`01_architecture.md` etc.)

---

## 2. High-level architecture overview

The Clarity Engine is a **document and lesson–oriented reasoning system** built around:

- a **core engine layer** (`engine_layer`, `rameon_core/engine`)  
- **edition and output logic** (`edition_logic`)  
- **lesson engine** (`lesson`, `flow_packs`, `template_packs`, `structure_packs`, `domain_packs`)  
- **routing and services** (`routing`, `src`)  
- **runtime and tests** (`rameon_core/runtime`, `tests`, `test_*`)  
- **UI and external interfaces** (`ui`, `server.py`, `src/api`, `src/cli`, `src/adapters`)

The architecture is **layered**, with clear separation between:

1. **Core engine and pipeline**  
2. **Domain and structure packs**  
3. **Lesson generation and teaching flows**  
4. **Edition and formatting logic**  
5. **Runtime, diagnostics, and tracing**  
6. **Interfaces and UI**

---

## 3. Repository structure as architecture backbone

The repository layout is itself an architectural map:

- `docs/` — human-readable documentation  
  - `01-overview/architecture.md` — high-level architecture summary  
  - `01-overview/glossary.md` — key terms  
  - `01-overview/lifecycle.md` — lifecycle and flows  
  - `02-core-engine/` — context, edition-logic, mappings, pipeline, resolvers  
  - `03-domain-packs/` — boundaries, examples, structure  
  - `04-runtime/` — error-handling, execution-flow, serialization, tracing, transforms, validation  
  - `05-interfaces/` — adapters, api, cli, formats  
  - `06-internal/` — keep-files, rules

- `engine_layer/` — primary engine layer implementation  
  - `dis.py`, `el3.py`–`el10.py`, `final_output.py`, `governance.py`, `osf.py`, `rameon.py`  
  - `engine_tests.py`, `simple_engine.py`, `quality.py`, `rewrite.py`, `sectioner.py`, `trace.py`  
  - `subsystems/naming_engine.py`

- `rameon_core/engine/` — core pipeline and diagnostics  
  - `context.py`, `pipeline.py`, `engine.py`, `sectioner.py`, `output_formatting.py`  
  - `dis1_detect_structure.py`–`dis5_section_detector.py`  
  - `el2_clarity_reorder.py`–`el9_export.py`, `el10_diagnostics.py`  
  - `tracing.py`, `test_full_pipeline.py`, `simple_engine.py`, `diagnostics.py`

- `lesson/` — lesson engine and teaching logic  
  - `lesson_architecture.py`, `lesson_generator.py`, `lesson_router.py`, `lesson_sections.py`  
  - `level_applier.py`, `level_router.py`, `topic_extractor.py`  
  - `grammar_profile.py`, `grammar_enricher.py`  
  - `error_profile.py`, `error_enricher.py`  
  - `cultural_profile.py`, `cultural_enricher.py`  
  - `vocab_profile.py`, `vocab_enricher.py`  
  - `guidance/` — guidance_enricher.py, guidance_profile.py, guidance_router.py

- `domain_packs/` — domain-level logic and validation  
  - `teaching_domain.py`, `core/`, `examples/`, `transforms/`, `validation/`

- `structure_packs/` — structural detection and teaching structures  
  - `teaching_structure.py`, DIS-related detectors

- `template_packs/` — canonical teaching templates  
  - `teaching_templates.py`

- `flow_packs/` — teaching flows  
  - `teaching_flow.py`

- `edition_logic/` — edition and output formatting  
  - `output_formatting.py`, `mappings/`, `resolvers/`, `rules/`

- `routing/` — domain routing  
  - `domain_router.py`

- `src/` — external interfaces  
  - `adapters/`, `api/`, `cli/`, `services/`

- `ui/` — browser UI  
  - `dashboard.html`, `dashboard.js`, `dashboard.css`, `index.html`, `script.js`, `style.css`, `ui.js`

- `tests/` and `test_*` — validation and integration tests  
- `main.py`, `server.py` — entry points and server runtime  
- `clarity_engine.py` — top-level engine wrapper

---

## 4. Layered architecture model

### 4.1 Engine layer and pipeline

**Core responsibilities:**

- Accept structured or semi-structured input (documents, lessons, prompts)  
- Detect structure and semantic units  
- Apply clarity, expression, and fusion transformations  
- Compose final outputs and exports  
- Provide diagnostics, tracing, and quality signals

**Key components:**

- **Structure detection (DIS series):**  
  - `dis1_detect_structure.py`  
  - `dis2_structure_detector.py`  
  - `dis3_block_detector.py`  
  - `dis4_semantic_unit_detector.py`  
  - `dis5_section_detector.py`

- **Engine pipeline (EL series):**  
  - `el2_clarity_reorder.py` — reorder content for clarity  
  - `el3_expression_shaping.py` — refine expression  
  - `el4_semantic_fusion.py` — merge semantic units  
  - `el5_output_composer.py` — assemble final structure  
  - `el6_final_polish.py` — polish language and formatting  
  - `el7_packaging.py` — package into target format  
  - `el8_validation.py` — validate structure and constraints  
  - `el9_export.py` — export to external formats  
  - `el10_diagnostics.py` — diagnostics and quality metrics

- **Engine orchestration:**  
  - `engine.py` — orchestrates pipeline stages  
  - `pipeline.py` — defines stage ordering and data flow  
  - `sectioner.py` — section-level segmentation  
  - `output_formatting.py` — formatting rules  
  - `trace.py` / `tracing.py` — tracing and logging  
  - `diagnostics.py` — engine diagnostics  
  - `quality.py` — quality scoring  
  - `rewrite.py` — rewrite operations  
  - `simple_engine.py` / `simple_engine_clean.py` — simplified engine variants

- **Governance and OSF:**  
  - `governance.py` — governance rules and constraints  
  - `osf.py` — Output Structure Framework (canonical output shapes)

### 4.2 Lesson engine and teaching architecture

**Purpose:**  
Transform user goals and language-learning needs into structured lesson plans, sections, and enriched content.

**Key flows:**

1. **Lesson architecture and routing:**  
   - `lesson_architecture.py` — defines lesson structure model  
   - `lesson_generator.py` — generates full lessons  
   - `lesson_router.py` — routes lesson requests to appropriate flows  
   - `lesson_sections.py` — defines section types and ordering  
   - `level_router.py` / `level_applier.py` — level selection and application  
   - `topic_extractor.py` — extract topics from input

2. **Profiles and enrichers:**  
   - **Grammar:** `grammar_profile.py`, `grammar_enricher.py`  
   - **Vocabulary:** `vocab_profile.py`, `vocab_enricher.py`  
   - **Error:** `error_profile.py`, `error_enricher.py`  
   - **Culture:** `cultural_profile.py`, `cultural_enricher.py`  
   - **Guidance:** `guidance_profile.py`, `guidance_enricher.py`, `guidance_router.py`

3. **Teaching flows and templates:**  
   - `flow_packs/teaching_flow.py` — canonical teaching flows  
   - `template_packs/teaching_templates.py` — lesson and trainer templates  
   - `structure_packs/teaching_structure.py` — teaching structure patterns

4. **Domain integration:**  
   - `domain_packs/teaching_domain.py` — teaching domain logic  
   - `domain_packs/core/`, `examples/`, `transforms/`, `validation/` — domain-specific rules and examples

### 4.3 Domain, structure, and template packs

**Domain packs (`domain_packs/`):**

- Provide **domain-specific rules**, examples, transforms, and validation logic.  
- Allow the engine to adapt to different operational domains (teaching, onboarding, SOP, etc.).  
- Are referenced by routing and engine layers to enforce domain constraints.

**Structure packs (`structure_packs/`):**

- Implement structural detection and teaching structures.  
- Extend DIS detectors for teaching-specific structures.  
- Provide reusable structural patterns for lessons and documents.

**Template packs (`template_packs/`):**

- Define canonical templates for lessons, trainers, and other outputs.  
- Ensure consistent formatting and section ordering.  
- Are used by `lesson_generator.py` and `output_formatting.py`.

**Flow packs (`flow_packs/`):**

- Encode teaching flows (e.g., warm-up → input → practice → feedback).  
- Provide reusable flow definitions for different lesson types.  
- Integrate with lesson routing and architecture.

---

## 5. Runtime, interfaces, and UI

### 5.1 Runtime and server

- `main.py` — main entry point for local runs or CLI usage.  
- `server.py` — server runtime, likely exposing HTTP or similar interface.  
- `clarity_engine.py` — top-level engine wrapper that coordinates engine_layer, lesson engine, and domain packs.  
- `rameon_core/runtime/` and `rameon_core/parsers/serializers/` — runtime helpers, parsing, and serialization.

### 5.2 External interfaces (`src/`)

- `src/adapters/` — integration adapters for external systems.  
- `src/api/` — API endpoints and request/response models.  
- `src/cli/` — command-line interface tools.  
- `src/services/` — service-level orchestration and business logic.

These interfaces sit **on top of** the engine and lesson layers, exposing capabilities to external consumers while respecting governance and OSF rules.

### 5.3 UI (`ui/`)

- `dashboard.html`, `dashboard.js`, `dashboard.css` — main dashboard UI.  
- `index.html`, `script.js`, `style.css`, `ui.js` — general UI and front-end logic.

The UI:

- Presents engine outputs (lessons, documents, diagnostics).  
- Allows users to trigger flows (lesson generation, analysis, exports).  
- Communicates with `server.py` / `src/api` to call engine functions.

---

## 6. Governance, invariants, and constraints

### 6.1 Governance layer

- `governance.py` and `docs/06-internal/rules.md` define **rules and constraints** that all engine operations must respect.  
- Governance ensures:
  - structural integrity of outputs  
  - compliance with domain rules  
  - consistency of naming and formatting  
  - safe and predictable behaviour

### 6.2 Output Structure Framework (OSF)

- `osf.py` and `docs/02-core-engine/mappings.md` / `pipeline.md` define canonical output structures.  
- OSF ensures:
  - outputs follow known patterns (tables, sections, headings, etc.)  
  - lesson and document shapes are predictable  
  - downstream consumers (UI, exports) can rely on stable formats.

### 6.3 Invariants

Core invariants include:

- **Deterministic pipeline ordering** — DIS → EL stages always run in defined sequence.  
- **Separation of concerns** — engine, lesson, domain, and UI layers remain isolated.  
- **Reconstruction alignment** — recovery kit architecture must be sufficient to rebuild this full architecture.  
- **Test-backed behaviour** — `tests/test_full_pipeline.py`, `test_engine.py`, `test_lesson_engine.py`, etc., validate behaviour.

---

## 7. Relationship to the recovery kit

The recovery kit (`recovery/01_architecture.md`, `02_philosophy.md`, `03_domains.md`, `04_business_roadmap.md`) provides:

- a **minimal rule-set** describing:
  - engine layering  
  - behavioural philosophy  
  - domain system  
  - business roadmap

This full architecture document:

- **expands** those minimal rules into concrete code-level structure.  
- **maps** each conceptual layer to actual modules and files.  
- **shows** how engine, lesson, domain, and UI components interact.  
- **anchors** Phase 2 system build to the already-tagged `recovery-v1.0` baseline.

---

## 8. Integration and extension points

Key extension points:

- **New domains:** add under `domain_packs/` and update routing and governance.  
- **New lesson types:** extend `lesson_sections.py`, `teaching_flow.py`, and templates.  
- **New output formats:** extend `output_formatting.py`, `osf.py`, and `el7_packaging.py`.  
- **New interfaces:** add under `src/api`, `src/cli`, or `src/adapters`.  
- **New diagnostics:** extend `diagnostics.py`, `quality.py`, `el10_diagnostics.py`, and tracing.

All extensions must:

- respect governance rules  
- align with OSF  
- preserve pipeline invariants  
- be covered by tests in `tests/` and `test_*` files.

---

## 9. Summary

This `architecture_full.md` file:

- describes the **complete operational architecture** of the Clarity Engine.  
- ties together repository structure, engine pipeline, lesson engine, domain packs, runtime, interfaces, and UI.  
- maintains alignment with the recovery kit while enabling rich Phase 2 system build.  
- provides a stable reference for future work on reasoning, teaching, workflows, and business logic.

