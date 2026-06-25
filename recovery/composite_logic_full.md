# Clarity Engine — Full Composite Logic Model (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **composite logic layer** of the Clarity Engine.  
Composite logic governs how the engine:

- combines multiple domains  
- merges multiple editions  
- generates multi‑document outputs  
- builds composite lesson packs  
- coordinates multi‑structure outputs  
- maintains isolation while supporting cross‑cutting tasks  

Composite logic sits **above domains and editions**, but **below governance**.

---

## 2. What composite logic is

### 2.1 Composite logic *is*:
- cross‑domain coordination  
- cross‑edition composition  
- multi‑document orchestration  
- multi‑structure output logic  
- pack‑level behaviour (e.g., lesson programmes, onboarding suites)  

### 2.2 Composite logic is *not*:
- a domain pack  
- an edition system  
- OSF or DIS  
- governance  
- runtime  

Composite logic **uses** these systems to build higher‑order outputs.

---

## 3. Composite scenarios

Composite logic applies to scenarios such as:

- generating a **multi‑lesson programme** from a single brief  
- producing **Trainer + Client + Cultural editions** as a coordinated set  
- building **onboarding A/B/C packs** as a single programme  
- creating **multi‑document business suites** (brief + SOP + onboarding + training)  
- handling **multi‑domain reasoning** (e.g., teaching + business + analysis)  

---

## 4. Composite lesson logic

### 4.1 Lesson programmes
Composite logic supports:

- multi‑lesson programmes  
- structured progression across lessons  
- consistent domain and edition behaviour across the set  

### 4.2 Components
Composite lesson logic uses:

- `lesson_architecture.py`  
- `lesson_generator.py`  
- `lesson/` enrichers  
- `flow_packs/` (teaching flows)  
- `template_packs/` (lesson templates)  

### 4.3 Behaviour
Composite logic ensures:

- each lesson is structurally valid (OSF, DIS, governance)  
- the programme has coherent progression  
- editions are correctly generated per lesson  

---

## 5. Composite onboarding logic

### 5.1 A/B/C packs
Composite logic coordinates:

- A Pack (skills)  
- B Pack (compliance)  
- C Pack (operational/SOP)  

### 5.2 Behaviour
Composite onboarding logic ensures:

- each pack is structurally valid  
- packs align with onboarding domain rules  
- the overall onboarding programme is coherent  

---

## 6. Composite business suites

Composite logic supports:

- brief + analysis + SOP + onboarding + training as a single suite  
- multi‑document generation from a single business context  

It ensures:

- each document respects its domain  
- cross‑document consistency (terminology, decisions, constraints)  
- governance validation per document  

---

## 7. Multi‑domain reasoning

Composite logic handles tasks that span multiple domains, such as:

- teaching + business communication  
- analysis + SOP  
- onboarding + training  

Rules:

- domains remain isolated at the document level  
- composite logic coordinates **which domain applies where**  
- governance validates each domain’s outputs separately  

---

## 8. Cross‑edition composition

Composite logic supports:

- generating multiple editions from a single semantic core  
- coordinating Trainer, Client, Cultural, Composite editions  

It uses:

- `edition_logic/`  
- `edition_logic/output_formatting.py`  
- edition resolvers  

Rules:

- semantic core is shared  
- formatting and content are edition‑specific  
- governance validates each edition independently  

---

## 9. Multi‑structure outputs

Composite logic can generate:

- packs of documents  
- suites of lessons  
- bundles of onboarding materials  

It uses:

- `structure_packs/`  
- `template_packs/`  
- `flow_packs/`  

Rules:

- each structure is valid on its own  
- composite sets are coherent and non‑contradictory  

---

## 10. Repository‑anchored composite logic

Composite logic is grounded in:

- `docs/03-domain-packs/composite.md` (if present)  
- `docs/01-overview/lifecycle.md` (multi‑document flows)  
- `lesson/` (programme generation)  
- `domain_packs/` (multi‑domain coordination)  
- `structure_packs/`, `template_packs/`, `flow_packs/`  
- `edition_logic/` (multi‑edition outputs)  

These components collectively implement composite behaviour.

---

## 11. Relationship to architecture, philosophy, domains, heuristics, soft knowledge, business knowledge, workflow knowledge, governance, runtime, interfaces, and integration

Composite logic:

- **uses** architecture to know what components exist  
- **respects** philosophy for behavioural consistency  
- **operates across** domains without breaking isolation  
- **leverages** heuristics and soft knowledge for natural behaviour  
- **applies** business and workflow knowledge for multi‑step programmes  
- **is constrained by** governance  
- **runs within** runtime and pipeline  
- **is exposed via** interfaces (API, CLI, UI)  
- **is documented by** integration  

Composite logic is the **higher‑order behaviour layer** that builds programmes, suites, and packs from the core engine.

---

## 12. Summary

This `composite_logic_full.md` file defines the Clarity Engine’s composite logic layer, including:

- multi‑lesson programmes  
- onboarding A/B/C packs  
- business document suites  
- multi‑domain reasoning  
- cross‑edition composition  
- multi‑structure outputs  
- repository‑anchored composite behaviour  

Composite logic governs *how the engine builds coherent sets of outputs* that span domains, editions, and structures while remaining fully governed and structurally valid.
