# Clarity Engine — Full Domain Encyclopedia (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **complete domain system** of the Clarity Engine.  
It expands the minimal recovery‑kit domain file into a full operational model covering:

- domain definitions  
- subdomains  
- boundaries and constraints  
- activation rules  
- domain switching logic  
- domain packs and structure packs  
- integration with the engine and lesson system  
- governance alignment  

This file governs *what domains exist* and *how they behave*.

---

## 2. What a domain is
A **domain** is a self‑contained behavioural and structural environment that defines:

- rules  
- constraints  
- templates  
- flows  
- structures  
- validation logic  
- examples  
- transforms  

Domains allow the engine to behave differently depending on the operational context (e.g., teaching vs onboarding vs SOP).

Domains are implemented in:

- `domain_packs/`  
- `structure_packs/`  
- `template_packs/`  
- `flow_packs/`  

and are routed via:

- `routing/domain_router.py`

---

## 3. Core domain list (Phase 2)
The Clarity Engine supports the following **primary domains**:

1. **Teaching Domain**  
2. **Lesson‑Plan Domain**  
3. **Self‑Learning Domain**  
4. **Onboarding Domain (A, B, C Packs)**  
5. **Operational / SOP Domain**  
6. **Business Communication Domain**  
7. **Analysis & Reasoning Domain**  
8. **Document Transformation Domain**  
9. **Product Design System Domain**  
10. **Runtime / Diagnostics Domain**  

Each domain is defined below.

---

## 4. Teaching Domain
### 4.1 Purpose
Supports language teaching, lesson generation, grammar/vocab enrichment, cultural adaptation, and structured pedagogy.

### 4.2 Key components
- `teaching_domain.py`  
- `lesson/` (architecture, generator, router, sections)  
- `flow_packs/teaching_flow.py`  
- `template_packs/teaching_templates.py`  
- `structure_packs/teaching_structure.py`  

### 4.3 Subdomains
- Grammar  
- Vocabulary  
- Error correction  
- Cultural adaptation  
- Guidance & feedback  

### 4.4 Constraints
- Must follow lesson structure rules  
- Must respect learner level  
- Must apply profiles and enrichers  
- Must maintain pedagogic clarity  

---

## 5. Lesson‑Plan Domain
### 5.1 Purpose
Generates structured lesson plans for trainers, including:

- objectives  
- warm‑ups  
- input  
- practice  
- feedback  
- homework  

### 5.2 Integration
Uses teaching templates but produces **trainer‑facing** outputs.

### 5.3 Constraints
- Must follow canonical lesson‑plan structure  
- Must be level‑appropriate  
- Must include trainer guidance  

---

## 6. Self‑Learning Domain
### 6.1 Purpose
Supports autonomous learners with:

- self‑study modules  
- reflective prompts  
- practice tasks  
- progress tracking  

### 6.2 Components
- Self‑Learning Domain Structure (v1.0)  
- Self‑study templates  
- Reflective frameworks  

### 6.3 Constraints
- Must avoid trainer‑specific instructions  
- Must support independent learning  

---

## 7. Onboarding Domain (A, B, C Packs)
### 7.1 Purpose
Supports organisational onboarding across three subdomains:

- **A Pack:** Skills‑based onboarding  
- **B Pack:** Compliance / regulatory onboarding  
- **C Pack:** Operational / SOP onboarding  

### 7.2 Components
- Onboarding Domain A Pack  
- Onboarding Domain B Pack  
- Onboarding Domain C Pack  

### 7.3 Constraints
- Must follow organisational structure  
- Must respect compliance rules  
- Must maintain clarity and accuracy  

---

## 8. Operational / SOP Domain
### 8.1 Purpose
Supports operational documentation:

- SOPs  
- workflows  
- checklists  
- procedures  
- operational guides  

### 8.2 Components
- Ops Domain Pack  
- SOP templates  
- Operational structure packs  

### 8.3 Constraints
- Must follow procedural clarity  
- Must avoid ambiguity  
- Must maintain step‑based structure  

---

## 9. Business Communication Domain
### 9.1 Purpose
Supports:

- emails  
- reports  
- briefs  
- summaries  
- stakeholder communication  

### 9.2 Components
- Business templates  
- Communication structures  
- Tone and clarity rules  

### 9.3 Constraints
- Must maintain professional tone  
- Must follow clarity and brevity rules  

---

## 10. Analysis & Reasoning Domain
### 10.1 Purpose
Supports:

- analytical documents  
- reasoning tasks  
- structured breakdowns  
- trade‑off analysis  
- decision frameworks  

### 10.2 Components
- Analysis templates  
- Reasoning structures  
- Diagnostic flows  

### 10.3 Constraints
- Must surface reasoning steps  
- Must avoid unsupported claims  

---

## 11. Document Transformation Domain
### 11.1 Purpose
Supports:

- rewriting  
- restructuring  
- summarisation  
- expansion  
- clarity enhancement  

### 11.2 Components
- DIS detectors  
- EL pipeline  
- OSF structures  

### 11.3 Constraints
- Must preserve meaning  
- Must maintain structural integrity  

---

## 12. Product Design System Domain
### 12.1 Purpose
Supports internal product documentation:

- design system  
- component definitions  
- naming conventions  
- architecture notes  

### 12.2 Components
- Clarity Product Design System  
- Reference material  
- Templates  

### 12.3 Constraints
- Must follow internal naming rules  
- Must maintain consistency across documents  

---

## 13. Runtime / Diagnostics Domain
### 13.1 Purpose
Supports:

- engine diagnostics  
- tracing  
- error handling  
- execution flow documentation  

### 13.2 Components
- `rameon_core/engine/diagnostics.py`  
- `rameon_core/engine/tracing.py`  
- Runtime documentation  

### 13.3 Constraints
- Must reflect actual engine behaviour  
- Must avoid speculative descriptions  

---

## 14. Domain boundaries
Domains must remain **strictly separated**.

A domain may not:

- borrow rules from another domain  
- leak templates across domains  
- mix flows or structures  
- violate governance constraints  

Boundaries are defined in:

- `docs/03-domain-packs/boundaries.md`  
- `domain_packs/core/`  
- `routing/domain_router.py`  

---

## 15. Domain activation rules
Domain activation is controlled by:

- `domain_router.py`  
- user intent  
- structural cues  
- explicit domain selection  

Activation rules:

1. Detect user intent  
2. Match to domain  
3. Load domain pack  
4. Apply domain constraints  
5. Generate output  

---

## 16. Domain switching logic
When switching domains:

- reset assumptions  
- clear domain‑specific context  
- load new domain pack  
- re‑evaluate user goal  
- apply new constraints  

Domain switching must be explicit and controlled.

---

## 17. Integration with engine and lesson system
Domains integrate with:

- **Engine Layer:** via OSF, DIS, EL pipeline  
- **Lesson Engine:** via templates, flows, structures  
- **Edition Logic:** via formatting and mapping rules  
- **Runtime:** via diagnostics and tracing  

Domains do not modify engine behaviour; they **configure** it.

---

## 18. Relationship to the recovery kit
The recovery‑kit domain file defines the **minimal domain model**.  
This full domain encyclopedia expands it into:

- detailed domain definitions  
- subdomains  
- boundaries  
- activation rules  
- switching logic  
- integration points  

It remains fully aligned with the recovery kit and can be reconstructed from it.

---

## 19. Summary
This `domains_full.md` file defines the complete domain system of the Clarity Engine, including:

- all domains and subdomains  
- boundaries and constraints  
- activation and switching rules  
- integration with engine, lesson, and runtime layers  
- alignment with governance and OSF  

It governs *what domains exist* and *how they behave* across the entire system.
