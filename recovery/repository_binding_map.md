# Clarity Engine — Repository Binding Map (Phase 3)

## 1. Purpose
This document maps the **system‑layer concepts** from the recovery files to the **actual repository structure**.  
It answers: *“Where does each idea live in code and docs?”*

---

## 2. Top‑level layout

**Core directories:**

- **`rameon_core/engine/`** — core runtime, pipeline, validation, tracing  
- **`engine_layer/`** — OSF, DIS, governance, constraints  
- **`lesson/`** — lesson architecture, generator, enrichers  
- **`domain_packs/`** — domain definitions and behaviours  
- **`structure_packs/`** — structural patterns (lesson, SOP, onboarding, etc.)  
- **`template_packs/`** — content templates  
- **`flow_packs/`** — multi‑step flows and workflows  
- **`src/api/`** — API interface  
- **`src/cli/`** — CLI interface  
- **`src/adapters/`** — external integrations  
- **`src/services/`** — internal services  
- **`server.py`** — server + routing  
- **`ui/`** — browser UI  
- **`docs/`** — system, domain, runtime, interface docs  

---

## 3. Binding recovery files to repo

### 3.1 Architecture (`architecture_full.md`)
- **Bound to:**
  - `rameon_core/engine/`  
  - `engine_layer/`  
  - `lesson/`  
  - `domain_packs/`, `structure_packs/`, `template_packs/`, `flow_packs/`  
  - `src/api/`, `src/cli/`, `src/adapters/`, `src/services/`  
  - `server.py`, `ui/`, `docs/`  

Architecture describes **what exists**; these directories implement it.

---

### 3.2 Philosophy (`philosophy_full.md`)
- **Bound to:**
  - `docs/01-overview/philosophy.md`  
  - behavioural comments and invariants in `rameon_core/engine/` and `engine_layer/`  

Philosophy governs **how components should behave**.

---

### 3.3 Domains (`domains_full.md`)
- **Bound to:**
  - `domain_packs/`  
  - `docs/03-domain-packs/`  

Domain packs implement the **actual domain logic**.

---

### 3.4 Heuristics & soft knowledge (`reasoning_heuristics.md`, `soft_knowledge.md`)
- **Bound to:**
  - heuristic modules in `rameon_core/engine/`  
  - enrichers and style modules in `lesson/`  

They shape **reasoning feel and tone**.

---

### 3.5 Business & workflow knowledge (`business_knowledge.md`, `workflow_knowledge.md`)
- **Bound to:**
  - business‑specific domain packs in `domain_packs/`  
  - flows in `flow_packs/`  
  - SOP/onboarding structures in `structure_packs/`  

They define **business behaviour and multi‑step flows**.

---

### 3.6 Governance (`governance_full.md`)
- **Bound to:**
  - `engine_layer/governance/`  
  - OSF/DIS enforcement modules  
  - validation and constraint logic in `rameon_core/engine/`  

Governance is implemented as **validators and constraint enforcers**.

---

### 3.7 Runtime (`runtime_full.md`)
- **Bound to:**
  - `rameon_core/engine/pipeline.py`  
  - runtime orchestration modules  
  - diagnostics and tracing components  

Runtime is the **execution pipeline**.

---

### 3.8 Interfaces (`interfaces_full.md`)
- **Bound to:**
  - `src/api/`  
  - `src/cli/`  
  - `src/adapters/`  
  - `server.py`  
  - `ui/`  
  - `docs/05-interfaces/`  

Interfaces are the **entry/exit points**.

---

### 3.9 Integration (`integration_full.md`)
- **Bound to:**
  - `docs/01-overview/` (lifecycle, system overview)  
  - cross‑layer glue in `rameon_core/engine/` and `engine_layer/`  

Integration explains **how all parts connect**.

---

### 3.10 Composite logic (`composite_logic_full.md`)
- **Bound to:**
  - `lesson/` (programmes, multi‑lesson sets)  
  - `structure_packs/`, `template_packs/`, `flow_packs/`  
  - multi‑document generators in `domain_packs/`  

Composite logic builds **packs, suites, programmes**.

---

### 3.11 Meta (`meta_full.md`)
- **Bound to:**
  - `docs/01-overview/meta.md` (if present)  
  - high‑level invariants and constraints across `docs/` and core modules  

Meta governs **self‑interpretation and system‑wide invariants**.

---

### 3.12 Recovery index (`recovery_index.md`)
- **Bound to:**
  - `docs/00-recovery/recovery_index.md` (master index)  

It is the **map of all recovery files**.

---

## 4. Role of this map

This Repository Binding Map:

- ties **concepts → directories**  
- ensures recovery docs are **anchored in code**  
- is the starting point for:
  - operational parameters  
  - lesson rules  
  - edition rules  
  - developer docs  
  - system manifest  

It is the **bridge** between the Phase 2 recovery layer and the Phase 3 operational layer.

---

## 5. Next step

With the binding map in place, the next Phase 3 file is:

- **`operational_parameters.md`** — where all **assumptions, numeric inputs, and scenario parameters** live.

If you want that next, just say: **Generate operational parameters file**.
