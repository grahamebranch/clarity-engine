# Meta‑Operational Rules — Clarity Engine (Phase 3)

## 1. Purpose
This document defines the **rules for modifying, extending, updating, or evolving** the Clarity Engine.  
It governs:

- how operational rules may change  
- how new domains or editions may be added  
- how templates and flows may evolve  
- how assumptions and parameters may be updated  
- how the recovery layer must be protected  
- how drift is prevented  

This is the **meta‑operational constitution** of the engine.

---

## 2. Scope

### 2.1 These rules apply to:
- operational parameters  
- lesson rules  
- edition rules  
- domain packs  
- structure packs  
- template packs  
- flow packs  
- developer documentation  
- interface documentation  

### 2.2 These rules do NOT apply to:
- architecture  
- philosophy  
- governance  
- meta  
- runtime  
- interfaces  
- integration  
- composite logic  
- recovery index  

Those belong to the **system layer** and are governed by Phase 2 meta rules.

---

## 3. Meta‑Operational Invariants

### 3.1 Structural Invariants
- The recovery layer must remain untouched unless system behaviour changes.  
- Operational rules must not contradict system‑layer rules.  
- No operational change may collapse domain or edition boundaries.  

### 3.2 Behavioural Invariants
- All operational changes must preserve determinism.  
- All operational changes must preserve CEFR alignment.  
- All operational changes must preserve governance compliance.  

### 3.3 Evolution Invariants
- The engine must remain reconstructible.  
- The engine must remain explainable.  
- The engine must remain stable across updates.  

---

## 4. Change Classification

Every change must be classified into one of four categories:

### 4.1 Type A — Operational Adjustment
Examples:
- updating adoption rates  
- adjusting vocabulary targets  
- modifying timing proportions  

Allowed if:
- it does not affect system behaviour  
- it does not violate governance  
- it is logged  

### 4.2 Type B — Operational Rule Update
Examples:
- modifying lesson rules  
- modifying edition rules  
- updating domain logic  

Allowed if:
- it does not contradict system layer  
- it passes validation  
- documentation is updated  

### 4.3 Type C — Operational Extension
Examples:
- adding a new domain pack  
- adding a new edition  
- adding a new flow pack  
- adding new templates  

Allowed if:
- it does not break isolation  
- it does not require system‑layer changes  
- it passes integration validation  

### 4.4 Type D — System‑Layer Impact
Examples:
- changes that affect architecture  
- changes that affect governance  
- changes that affect meta rules  

These are **not allowed** in Phase 3.  
They require a **Phase 4 system‑layer revision cycle**.

---

## 5. Update Workflow (Authoritative)

### Step 1 — Identify Change Type
Classify as A, B, C, or D.

### Step 2 — Check System‑Layer Constraints
Verify:
- architecture  
- philosophy  
- governance  
- meta  

If the change violates any of these → **stop**.

### Step 3 — Implement Change
Apply change in the correct repo directory using the binding map.

### Step 4 — Validate
Run:
- OSF validation  
- DIS validation  
- governance validation  
- edition validation  
- domain validation  

### Step 5 — Update Documentation
Update:
- operational parameters  
- lesson rules  
- edition rules  
- domain docs  
- developer docs  

### Step 6 — Log Change
Record:
- what changed  
- why  
- classification  
- validation results  

---

## 6. Drift Prevention Rules

### 6.1 Terminology Drift
Forbidden:
- renaming sections  
- renaming edition types  
- renaming domain packs  
- renaming structural components  

### 6.2 Behavioural Drift
Forbidden:
- altering lesson structure  
- altering CEFR alignment  
- altering edition invariants  

### 6.3 Conceptual Drift
Forbidden:
- mixing system‑layer logic into operational files  
- mixing operational logic into system‑layer files  

---

## 7. Extension Rules

### 7.1 Adding a New Domain
Allowed if:
- domain is isolated  
- domain has its own templates  
- domain has its own flows  
- domain does not conflict with existing domains  

### 7.2 Adding a New Edition
Allowed if:
- edition rules are fully defined  
- edition is isolated  
- edition does not break invariants  
- edition passes governance  

### 7.3 Adding New Templates or Flows
Allowed if:
- templates follow structure pack rules  
- flows follow workflow rules  
- no cross‑domain leakage occurs  

---

## 8. Parameter Update Rules

### 8.1 Allowed
- adoption rates  
- pricing assumptions  
- conversion rates  
- timing proportions  
- vocabulary targets  

### 8.2 Forbidden
- modifying system invariants  
- modifying CEFR definitions  
- modifying governance rules  

### 8.3 Requirements
- must be logged  
- must be justified  
- must be scenario‑aligned  

---

## 9. Validation Rules

### 9.1 Mandatory Validation
Every operational change must pass:
- OSF  
- DIS  
- governance  
- edition validation  
- domain validation  

### 9.2 Failure Handling
If validation fails:
- revert change  
- log failure  
- classify reason  
- propose alternative  

---

## 10. Summary
This document defines the **meta‑operational rules** that govern how the Clarity Engine evolves.  
It ensures:

- safe updates  
- controlled evolution  
- no drift  
- no contradictions  
- no system‑layer violations  
- full reconstructability  

This is the **constitution for modifying the operational layer**.

