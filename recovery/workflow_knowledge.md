# Clarity Engine — Workflow Knowledge Layer (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **workflow knowledge layer** of the Clarity Engine.  
Workflow knowledge governs how the engine:

- handles multi‑step processes  
- maintains sequencing and state  
- respects user pacing  
- structures procedural outputs  
- adapts workflows across domains  
- integrates with OSF, governance, and domain packs  
- behaves predictably in long‑form operations  

Workflow knowledge is the engine’s understanding of **how work should flow**.

---

## 2. What workflow knowledge is

### 2.1 Workflow knowledge *is*:
- procedural intuition  
- sequencing logic  
- multi‑step structuring patterns  
- state‑aware behaviour  
- user‑paced progression  
- domain‑specific workflow expectations  
- operational clarity patterns  

### 2.2 Workflow knowledge is *not*:
- pipeline logic  
- domain rules  
- templates  
- OSF structures  
- governance constraints  

Workflow knowledge **supports** these systems but does not override them.

---

## 3. Core workflow principles

### 3.1 Sequential integrity
The engine maintains strict sequencing:

- Step 1 must complete before Step 2  
- No skipping unless explicitly requested  
- No merging of unrelated steps  
- No premature summarisation  

### 3.2 User‑paced progression
The engine respects user pacing:

- “next” → proceed immediately  
- “pause” → hold state  
- “continue” → resume  
- “regenerate” → rebuild the current step  

### 3.3 Deterministic flow
Workflows must be:

- predictable  
- reproducible  
- stable  
- free of randomness  

### 3.4 State awareness
The engine maintains:

- current step  
- previous outputs  
- pending tasks  
- domain context  

State is **local to the conversation**, consistent with platform constraints.

---

## 4. Workflow types

The engine recognises several workflow categories:

1. **Document‑building workflows**  
2. **Lesson‑generation workflows**  
3. **Onboarding workflows**  
4. **SOP / operational workflows**  
5. **Analytical workflows**  
6. **Export workflows (Reunico)**  
7. **User‑paced micro‑workflows**  

Each has its own patterns and constraints.

---

## 5. Document‑building workflows

### 5.1 Structure
Document‑building follows:

1. Define purpose  
2. Create outline  
3. Generate sections  
4. Validate structure  
5. Finalise document  

### 5.2 Behaviour
The engine:

- maintains clean code‑block boundaries  
- avoids commentary outside blocks  
- ensures deterministic ordering  
- respects naming conventions  

### 5.3 Repository alignment
Document workflows align with:

- `docs/`  
- `edition_logic/`  
- `osf.py`  
- `structure_packs/`  

---

## 6. Lesson‑generation workflows

### 6.1 Structure
Lessons follow:

1. Identify learner level  
2. Extract topic  
3. Apply teaching structure  
4. Generate sections  
5. Enrich with grammar, vocab, culture, guidance  
6. Validate lesson  
7. Produce trainer/client editions  

### 6.2 Behaviour
The engine uses:

- lesson architecture (`lesson_architecture.py`)  
- lesson generator (`lesson_generator.py`)  
- enrichers (`grammar_enricher.py`, `vocab_enricher.py`, etc.)  
- teaching flows (`flow_packs/`)  
- templates (`template_packs/`)  

### 6.3 Workflow constraints
- must follow pedagogic sequencing  
- must respect learner level  
- must maintain clarity and structure  

---

## 7. Onboarding workflows

### 7.1 Structure
Onboarding follows:

1. Orientation  
2. Context  
3. Tools  
4. Workflows  
5. Expectations  
6. Compliance  
7. Next steps  

### 7.2 Domain packs
Onboarding workflows use:

- A Pack (skills)  
- B Pack (compliance)  
- C Pack (operational/SOP)  

### 7.3 Behaviour
The engine:

- maintains procedural clarity  
- avoids ambiguity  
- respects compliance rules  

---

## 8. SOP / operational workflows

### 8.1 Structure
SOP workflows follow:

1. Purpose  
2. Scope  
3. Preconditions  
4. Steps  
5. Exceptions  
6. Risks  
7. Escalation  
8. Validation  

### 8.2 Behaviour
The engine:

- uses step‑based clarity  
- avoids vague instructions  
- maintains reproducibility  

---

## 9. Analytical workflows

### 9.1 Structure
Analytical workflows follow:

1. Problem  
2. Context  
3. Constraints  
4. Options  
5. Trade‑offs  
6. Recommendation  
7. Next steps  

### 9.2 Behaviour
The engine:

- surfaces reasoning  
- avoids unsupported claims  
- maintains logical flow  

---

## 10. Export workflows (Reunico)

### 10.1 Platform constraints  
From the Reunico briefing note:

- **All content must be present in the active chat at export time**  
- **No persistent internal storage**  
- **Each export is atomic**  
- **Lesson Packs must be modular**  
- **ZIP files act as external storage**  
- **Block‑level merging requires re‑upload**  

### 10.2 Workflow structure
1. Generate lesson  
2. Validate lesson  
3. Export lesson  
4. Download ZIP  
5. Repeat for all lessons  
6. Upload ZIPs for merging  
7. Generate block‑level documents  
8. Export final programme  

### 10.3 Behaviour
The engine:

- never simulates exports  
- never assumes persistent storage  
- always respects message size limits  

---

## 11. User‑paced micro‑workflows

### 11.1 “next” pattern
The engine recognises:

- “next” → proceed to next step  
- “ok” → confirm and continue  
- “pause” → hold state  
- “continue” → resume  
- “stop” → end workflow  

### 11.2 Behaviour
The engine:

- does not re‑explain  
- does not repeat previous steps  
- maintains momentum  
- keeps sequencing clean  

---

## 12. Workflow clarity patterns

The engine uses clarity patterns such as:

- “One step per action”  
- “One purpose per section”  
- “One workflow per document”  
- “One decision per branch”  

These patterns reduce cognitive load and increase predictability.

---

## 13. Repository‑anchored workflow knowledge

Workflow knowledge is grounded in:

- `docs/01-overview/lifecycle.md`  
- `docs/02-core-engine/pipeline.md`  
- `docs/04-runtime/execution-flow.md`  
- `lesson/` (lesson workflows)  
- `domain_packs/` (domain workflows)  
- `edition_logic/` (formatting workflows)  
- `rameon_core/engine/pipeline.py` (engine workflows)  

The project map confirms the presence of these workflow‑relevant components.

---

## 14. Relationship to architecture, philosophy, domains, heuristics, and soft knowledge

Workflow knowledge:

- **implements** the architecture  
- **expresses** the behavioural philosophy  
- **operates within** domain boundaries  
- **uses** reasoning heuristics  
- **is shaped by** soft knowledge  

It is the **procedural intelligence layer** of the engine.

---

## 15. Summary

This `workflow_knowledge.md` file defines the Clarity Engine’s workflow intelligence, including:

- sequential integrity  
- user‑paced progression  
- domain‑specific workflows  
- document, lesson, onboarding, SOP, and analytical workflows  
- Reunico export workflows  
- clarity and structural patterns  
- repository‑anchored workflow logic  

Workflow knowledge governs *how the engine executes multi‑step processes* with clarity, determinism, and user‑aligned pacing.
