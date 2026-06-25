# Recovery Kit Manifest — Clarity Engine (Phase 3)

## 1. Purpose
This manifest defines the **complete structure, contents, and reconstruction order** of the Clarity Engine Recovery Kit.  
It ensures that the engine can be:

- rebuilt  
- audited  
- validated  
- transferred  
- versioned  
- restored  

…from first principles, using only the recovery files.

---

## 2. Recovery Kit Overview

The Recovery Kit contains **all system‑layer documents** required to reconstruct the engine without access to the operational layer, domain packs, templates, or flows.

It includes:

- architecture  
- philosophy  
- domains  
- heuristics  
- soft knowledge  
- business knowledge  
- workflow knowledge  
- governance  
- runtime  
- interfaces  
- integration  
- composite logic  
- meta  
- recovery index  
- meta‑operational rules  
- repository binding map  
- operational parameters (optional for reconstruction)  

---

## 3. Recovery Kit Contents (Authoritative)

### 3.1 System‑Layer Files (Phase 2)
1. `architecture_full.md`  
2. `philosophy_full.md`  
3. `domains_full.md`  
4. `reasoning_heuristics.md`  
5. `soft_knowledge.md`  
6. `business_knowledge.md`  
7. `workflow_knowledge.md`  
8. `governance_full.md`  
9. `runtime_full.md`  
10. `interfaces_full.md`  
11. `integration_full.md`  
12. `composite_logic_full.md`  
13. `meta_full.md`  
14. `recovery_index.md`  

### 3.2 Phase‑3 Binding & Operational Files
15. `repository_binding_map.md`  
16. `meta_operational_rules.md`  
17. `operational_parameters.md`  

### 3.3 Optional (Non‑System) Files
18. `lesson_rules_full.md`  
19. `edition_rules_full.md`  
20. `developer_guide.md`  

These are not required for reconstruction but are included for completeness.

---

## 4. Reconstruction Order (Mandatory)

To rebuild the engine:

1. Load `architecture_full.md`  
2. Apply `philosophy_full.md`  
3. Load `domains_full.md`  
4. Apply `reasoning_heuristics.md`  
5. Apply `soft_knowledge.md`  
6. Apply `business_knowledge.md`  
7. Apply `workflow_knowledge.md`  
8. Enforce `governance_full.md`  
9. Run `runtime_full.md`  
10. Bind `interfaces_full.md`  
11. Apply `integration_full.md`  
12. Apply `composite_logic_full.md`  
13. Apply `meta_full.md`  
14. Validate using `recovery_index.md`  
15. Bind to repo using `repository_binding_map.md`  
16. Apply `meta_operational_rules.md`  
17. Load `operational_parameters.md` (optional)  

This sequence is **deterministic** and **complete**.

---

## 5. Versioning Rules

### 5.1 Version Format
`recovery-vMAJOR.MINOR`

Examples:
- `recovery-v1.0`  
- `recovery-v1.1`  
- `recovery-v2.0`  

### 5.2 Version Increments
- **MAJOR** increments when system‑layer behaviour changes.  
- **MINOR** increments when operational rules change.  

### 5.3 Tagging Rules
- Every recovery kit must be tagged.  
- Tags must be immutable.  
- Tags must match manifest version.  

---

## 6. Integrity Rules

### 6.1 Completeness
All files listed in Section 3 must exist.

### 6.2 Coherence
Files must not contradict each other.

### 6.3 Ordering
Reconstruction must follow Section 4.

### 6.4 Validation
Recovery kit must pass:
- OSF  
- DIS  
- governance  
- meta  

### 6.5 Drift Prevention
No file may:
- redefine system invariants  
- redefine architecture  
- redefine philosophy  
- collapse domain or edition boundaries  

---

## 7. Export Rules

### 7.1 Export Format
The recovery kit may be exported as:
- a folder  
- a compressed archive  
- a versioned release  

### 7.2 Export Requirements
Exports must include:
- all system‑layer files  
- this manifest  
- version tag  

### 7.3 Export Exclusions
Exports must NOT include:
- domain packs  
- templates  
- flows  
- operational code  
- UI  
- API  

---

## 8. Summary
This manifest defines the **complete, authoritative structure** of the Clarity Engine Recovery Kit.  
It ensures the engine can always be:

- reconstructed  
- validated  
- versioned  
- transferred  
- audited  

…using only the recovery files.

