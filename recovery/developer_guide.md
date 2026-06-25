# Developer Guide — Clarity Engine (Phase 3)

## 1. Purpose
This guide provides developers with the **operational rules, workflows, and expectations** for contributing to the Clarity Engine.  
It ensures:

- consistency  
- stability  
- governance compliance  
- edition isolation  
- domain isolation  
- reproducibility  

This is the **primary onboarding document** for all developers.

---

## 2. Core Principles

### 2.1 Determinism
All engine behaviour must be deterministic.  
No randomness.  
No hidden state.

### 2.2 Isolation
- Domains must be isolated.  
- Editions must be isolated.  
- System layer must be isolated from operational layer.  

### 2.3 Governance First
All changes must pass governance validation before merging.

### 2.4 Recovery Integrity
The engine must always be reconstructible from the recovery layer.

---

## 3. Repository Structure (Developer View)

### 3.1 Core Engine
- `rameon_core/engine/` — runtime, pipeline, validation  
- `engine_layer/` — OSF, DIS, governance  

### 3.2 Content & Logic
- `lesson/` — lesson generator, enrichers  
- `domain_packs/` — domain logic  
- `structure_packs/` — structural patterns  
- `template_packs/` — templates  
- `flow_packs/` — multi‑step flows  

### 3.3 Interfaces
- `src/api/`  
- `src/cli/`  
- `src/adapters/`  
- `src/services/`  
- `server.py`  
- `ui/`  

### 3.4 Documentation
- `docs/` — system, domain, runtime, interface docs  
- `docs/00-recovery/` — recovery layer  

---

## 4. Development Workflow

### 4.1 Step 1 — Understand the Layer You Are Modifying
Every change must be classified as:

- system layer  
- operational layer  
- domain layer  
- edition layer  
- interface layer  
- runtime layer  

### 4.2 Step 2 — Check Recovery Layer
Before modifying anything, check:

- architecture  
- philosophy  
- domains  
- governance  
- meta  

If your change violates any of these, it is **not allowed**.

### 4.3 Step 3 — Implement Change in Repo
Follow the binding map to locate the correct directory.

### 4.4 Step 4 — Validate
Run:

- OSF validation  
- DIS validation  
- governance validation  
- edition validation  
- domain validation  

### 4.5 Step 5 — Update Documentation
If behaviour changes, update:

- operational docs  
- domain docs  
- edition docs  
- recovery docs (only if system behaviour changes)  

### 4.6 Step 6 — Log Change
Every change must be logged in the change register.

---

## 5. Coding Standards

### 5.1 Style
- clean  
- readable  
- explicit  
- no magic numbers  
- no hidden state  

### 5.2 Functions
- pure where possible  
- side‑effects must be documented  
- inputs/outputs must be typed  

### 5.3 Error Handling
- use engine‑layer error types  
- no silent failures  
- no generic exceptions  

### 5.4 Comments
- explain *why*, not *what*  
- reference recovery docs when relevant  

---

## 6. Domain Development Rules

### 6.1 Domain Isolation
Domains must not:
- call each other  
- share state  
- share templates  

### 6.2 Domain Packs
Each domain pack must include:
- domain definition  
- domain rules  
- domain templates  
- domain flows (optional)  

### 6.3 Domain Validation
Domains must pass:
- domain isolation checks  
- CEFR alignment checks  
- edition compatibility checks  

---

## 7. Edition Development Rules

### 7.1 Edition Isolation
Editions must not:
- modify semantic core  
- modify lesson structure  
- override CEFR rules  

### 7.2 Edition Logic
Edition logic must:
- transform tone  
- transform detail  
- transform formatting  
- preserve meaning  

### 7.3 Edition Validation
Each edition must pass:
- OSF  
- DIS  
- governance  
- edition‑specific rules  

---

## 8. Lesson Engine Development Rules

### 8.1 Lesson Structure
The structure defined in `lesson_rules_full.md` is **mandatory**.

### 8.2 Lesson Generator
The generator must:
- produce a neutral semantic core  
- apply lesson rules  
- expose edition‑ready content  

### 8.3 Enrichers
Enrichers must:
- be deterministic  
- be CEFR‑aligned  
- not introduce bias  

---

## 9. Testing Requirements

### 9.1 Unit Tests
Required for:
- domain logic  
- edition logic  
- enrichers  
- validators  

### 9.2 Integration Tests
Required for:
- lesson generation  
- multi‑step flows  
- API endpoints  

### 9.3 Regression Tests
Required when:
- updating templates  
- updating domain rules  
- updating edition rules  

---

## 10. Governance Compliance

### 10.1 Mandatory Checks
All changes must pass:
- OSF  
- DIS  
- governance  
- meta  

### 10.2 Forbidden Changes
Developers may NOT:
- modify system invariants  
- modify architecture  
- modify philosophy  
- bypass governance  
- collapse domain boundaries  
- collapse edition boundaries  

---

## 11. Developer Responsibilities

### 11.1 Required
- follow this guide  
- follow recovery layer  
- follow binding map  
- document changes  
- validate changes  

### 11.2 Forbidden
- ad‑hoc changes  
- undocumented behaviour  
- unvalidated behaviour  
- cross‑domain leakage  
- edition drift  

---

## 12. Summary
This guide defines the **operational rules** for developing the Clarity Engine.  
It ensures:

- stability  
- consistency  
- governance compliance  
- deterministic behaviour  
- safe evolution  

This is the **primary onboarding and operational manual** for all developers.

