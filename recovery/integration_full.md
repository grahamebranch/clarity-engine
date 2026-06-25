# Clarity Engine — Full Integration Model (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **integration layer** of the Clarity Engine.  
Integration explains how:

- architecture  
- philosophy  
- domains  
- reasoning heuristics  
- soft knowledge  
- business knowledge  
- workflow knowledge  
- governance  
- runtime  
- interfaces  

all connect into a single coherent system.

---

## 2. What integration is

### 2.1 Integration *is*:
- cross‑layer coordination  
- responsibility mapping  
- interaction rules  
- dependency structure  
- recovery logic  

### 2.2 Integration is *not*:
- a separate engine  
- a domain pack  
- a template system  
- a runtime module  

Integration **describes** how existing parts work together.

---

## 3. Core integration principles

### 3.1 Single source of truth
- Architecture defines structure.  
- Philosophy defines behaviour.  
- Domains define scope.  
- Governance enforces constraints.  
- Runtime executes flows.  
- Interfaces expose the system.

### 3.2 Layered responsibility
Each layer has a clear role:

- **Architecture:** what exists.  
- **Philosophy:** how it should behave.  
- **Domains:** where behaviour applies.  
- **Heuristics & soft knowledge:** how reasoning feels.  
- **Business & workflow knowledge:** how work is done.  
- **Governance:** what is allowed.  
- **Runtime:** how it runs.  
- **Interfaces:** how it is accessed.

### 3.3 Non‑overlap
Layers must not:

- duplicate responsibilities  
- override each other’s core role  
- introduce hidden logic  

---

## 4. Integration map (repository‑anchored)

Integration is grounded in:

- `docs/01-overview/` (system overview, lifecycle)  
- `docs/02-core-engine/` (architecture, pipeline, edition logic)  
- `docs/03-domain-packs/` (domain boundaries, packs)  
- `docs/04-runtime/` (execution flow, diagnostics)  
- `docs/05-interfaces/` (API, CLI, adapters, UI)  
- `rameon_core/engine/` (runtime, pipeline, validation, tracing)  
- `engine_layer/` (OSF, DIS, governance)  
- `lesson/` (lesson architecture, generator, enrichers)  
- `domain_packs/`, `structure_packs/`, `template_packs/`, `flow_packs/`  

These directories collectively implement the integrated system.

---

## 5. Cross‑layer interactions

### 5.1 Architecture ↔ Runtime
- Architecture defines components.  
- Runtime orchestrates them.  
- Pipeline (`pipeline.py`) is the bridge.

### 5.2 Domains ↔ OSF/DIS
- Domains define scope and rules.  
- DIS detects domain instructions.  
- OSF structures outputs.  
- Governance ensures domain and structure alignment.

### 5.3 Heuristics & soft knowledge ↔ Runtime
- Heuristics guide reasoning.  
- Soft knowledge shapes “feel”.  
- Runtime applies both during execution.  
- Governance overrides them when constraints conflict.

### 5.4 Business & workflow knowledge ↔ Domains
- Business knowledge configures behaviour in business contexts.  
- Workflow knowledge structures multi‑step processes.  
- Domain packs provide the rules.  
- Flows (`flow_packs/`) implement domain‑specific workflows.

### 5.5 Governance ↔ Everything
- Governance validates domain, edition, structure, constraints, and safety.  
- It is the final arbiter before output.  
- No layer can bypass governance.

### 5.6 Interfaces ↔ Runtime
- Interfaces send requests to runtime.  
- Runtime processes them via pipeline.  
- Interfaces return structured outputs.  
- Interfaces must preserve structure and metadata.

---

## 6. Recovery integration

### 6.1 Recovery layer
The recovery layer consists of:

- `architecture_full.md`  
- `philosophy_full.md`  
- `domains_full.md`  
- `reasoning_heuristics.md`  
- `soft_knowledge.md`  
- `business_knowledge.md`  
- `workflow_knowledge.md`  
- `governance_full.md`  
- `runtime_full.md`  
- `interfaces_full.md`  
- `integration_full.md`  

These files together define the **minimal canonical description** of the system.

### 6.2 Recovery process
From the recovery layer, the engine can be reconstructed by:

1. Rebuilding architecture from `architecture_full.md`.  
2. Restoring behavioural philosophy from `philosophy_full.md`.  
3. Reinstating domains from `domains_full.md`.  
4. Reapplying heuristics and soft knowledge.  
5. Reconfiguring business and workflow knowledge.  
6. Re‑establishing governance and OSF/DIS.  
7. Recreating runtime and pipeline.  
8. Rebinding interfaces.  
9. Validating integration via this document.

---

## 7. Integration invariants

Integration enforces invariants such as:

- **No domain without governance.**  
- **No output without OSF and DIS.**  
- **No edition without edition logic.**  
- **No workflow without domain and constraints.**  
- **No interface without runtime.**  
- **No behaviour without philosophy.**

These invariants prevent drift and fragmentation.

---

## 8. Drift prevention

Integration prevents drift by:

- centralising cross‑layer rules in `docs/01-overview/` and this file.  
- ensuring each layer has a single, documented purpose.  
- making recovery files the canonical reference.  
- avoiding undocumented behaviour.  

---

## 9. Relationship to all other layers

Integration:

- **binds** architecture, philosophy, domains, heuristics, soft knowledge, business knowledge, workflow knowledge, governance, runtime, and interfaces.  
- **documents** how they interact.  
- **ensures** the system is reconstructible from the recovery layer.  

It is the **system coherence document**.

---

## 10. Summary

This `integration_full.md` file defines the Clarity Engine’s integration layer, including:

- cross‑layer responsibility mapping  
- interaction rules  
- repository‑anchored integration map  
- recovery logic  
- invariants and drift prevention  

Integration governs *how the entire system hangs together* as a single, coherent, reconstructible engine.
