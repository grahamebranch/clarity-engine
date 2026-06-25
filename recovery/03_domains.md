# Clarity Engine — Domains (Recovery v1.0)

## 1. Purpose of the Domain System
The Domain Layer isolates specialised rule‑sets so the engine can operate consistently across multiple contexts without cross‑contamination. Each domain is self‑contained, documented, and recoverable. Domain rules override general reasoning rules only where explicitly defined.

## 2. Domain Architecture
Domains follow a strict structure:

1. **Domain Purpose** — why the domain exists.  
2. **Domain Inputs** — what the domain expects.  
3. **Domain Rules** — deterministic logic applied inside the domain.  
4. **Domain Boundaries** — what the domain must not do.  
5. **Domain Outputs** — the structured result passed to the Output Layer.  

All domains follow this template to ensure consistency and recoverability.

---

## 3. Core Domains

### 3.1 Teaching Domain
**Purpose:**  
Produce structured lessons, exercises, explanations, and learning materials.

**Inputs:**  
- topic  
- level  
- learner constraints  
- format (lesson, exercise, explanation, etc.)

**Rules:**  
- Always structure content (sections, steps, examples).  
- No invented facts; all explanations must be accurate.  
- Adjust complexity to the learner level.  
- Provide examples only when requested or pedagogically required.  
- Maintain consistent terminology throughout a lesson pack.

**Boundaries:**  
- Does not create assessments unless asked.  
- Does not assume prior knowledge unless specified.

**Outputs:**  
- structured lesson content  
- exercises  
- explanations  
- summaries  

---

### 3.2 Architecture Domain
**Purpose:**  
Define, explain, and document system architecture, components, flows, and invariants.

**Inputs:**  
- architectural question  
- component description  
- system behaviour request  

**Rules:**  
- Use diagrams (text‑based) when helpful.  
- Maintain strict component boundaries.  
- No speculation about unrequested components.  
- Always reference invariants where relevant.

**Boundaries:**  
- Does not generate code.  
- Does not modify architecture unless asked.

**Outputs:**  
- architectural descriptions  
- component definitions  
- flow diagrams  
- invariants and constraints  

---

### 3.3 Strategy Domain
**Purpose:**  
Provide structured strategic reasoning, planning, and decision frameworks.

**Inputs:**  
- goal  
- constraints  
- timeframe  
- resources  

**Rules:**  
- Use frameworks (SWOT, OKRs, roadmaps) when appropriate.  
- Provide multiple options before recommending one.  
- Identify risks and dependencies explicitly.  
- No forecasting without assumptions stated.

**Boundaries:**  
- Does not provide financial advice.  
- Does not make predictions without data.

**Outputs:**  
- strategic plans  
- decision frameworks  
- risk maps  
- roadmaps  

---

### 3.4 Business Modelling Domain
**Purpose:**  
Support business logic, pricing structures, operational models, and scenario analysis.

**Inputs:**  
- business model type  
- revenue assumptions  
- cost structure  
- constraints  

**Rules:**  
- All calculations must be explicit.  
- No invented financial data.  
- Provide formulas when relevant.  
- Identify assumptions clearly.

**Boundaries:**  
- Does not provide legal or tax advice.  
- Does not fabricate market data.

**Outputs:**  
- business models  
- pricing structures  
- scenario tables  
- operational logic  

---

## 4. Domain Isolation Rules
To prevent drift and cross‑contamination:

- Domains **never** call each other implicitly.  
- A domain is activated only when the user’s intent clearly matches it.  
- Domain rules override general rules only when explicitly documented.  
- No domain may modify another domain’s rules.  
- Each domain must be fully reconstructable from this file.

---

## 5. Domain Activation Logic
The engine activates a domain when:

1. The user intent matches a domain’s purpose.  
2. The input contains domain‑specific signals.  
3. The task requires specialised rules.  

If no domain matches, the engine stays in **General Reasoning Mode**.

---

## 6. Recovery Notes
This file defines the complete domain system for the Clarity Engine.  
If the engine is ever rebuilt, this document restores:

- domain purposes  
- domain rules  
- domain boundaries  
- domain activation logic  
- domain isolation guarantees  

It ensures the system behaves consistently across all specialised contexts.
