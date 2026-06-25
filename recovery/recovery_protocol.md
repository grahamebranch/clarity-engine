# Recovery Protocol — Clarity Engine (Four-Layer Model)
Snapshot ID: REC-2026-06-25-01  
Snapshot Date: 2026-06-25  
Environment: Production

Required Layers:
- Engine Snapshot: ENG-2026-06-25-01  
- Operational Parameters Snapshot: OP-2026-06-25-01  
- Business Context Snapshot: BC-2026-06-25-01  
- Business Values Snapshot: BV-2026-06-25-01  

---

# 1. Purpose
This protocol defines the **authoritative sequence** for fully restoring the Clarity Engine, including:

- system architecture  
- operational assumptions  
- business reasoning  
- numerical modelling values  

A complete recovery requires **all four layers**.

---

# 2. Recovery Sequence (Authoritative)

## Step 1 — Rebuild Engine (Canonical)
Load **Phases 1–18** in strict order.

This restores:
- architecture  
- invariants  
- governance  
- runtime  
- export logic  
- lifecycle logic  

Then:
- run canonical test suite  
- run self-audit  
- confirm invariants and governance integrity  

The engine must be fully functional before loading any business layers.

---

## Step 2 — Load Operational Parameters
Load `operational_parameters.md` (OP-2026-06-25-01).

This restores:
- adoption assumptions  
- pricing assumptions  
- cost assumptions  
- lesson engine operational settings  
- edition behaviour parameters  
- scenario definitions  

Rules:
- parameters **must not** modify architecture  
- parameters **must** be compatible with governance  
- parameters **must** be validated before use  

---

## Step 3 — Load Business Context
Load `business_context.md` (BC-2026-06-25-01).

This restores:
- strategic intent  
- worldview  
- decision logic  
- human values  
- reasoning environment  
- historical decisions  
- risk posture  
- market understanding  

This step restores the **state of mind** of the project at the snapshot date.

---

## Step 4 — Load Business Values
Load `business_values.md` (BV-2026-06-25-01).

This restores:
- adoption values  
- churn values  
- conversion values  
- pricing values  
- cost values  
- revenue values  
- scenario multipliers  
- sensitivity weights  
- roadmap priority weights  
- monthly and yearly forecast values  

Rules:
- values must not contradict operational parameters  
- values must be internally consistent  
- values must be validated before modelling  

---

## Step 5 — Regenerate Derived Business Views
Derived views are **not canonical** and must be regenerated from layers 2–4.

Regenerate:
- roadmap  
- forecast  
- pricing model  
- adoption curves  
- risk models  
- scenario outputs  

These outputs are **ephemeral** and must never be stored as canonical files.

---

# 3. Integrity Rules

### 3.1 Layer Boundaries
- Engine layer cannot be modified by business layers.  
- Operational parameters cannot override system rules.  
- Business context cannot override governance.  
- Business values cannot override operational parameters.  

### 3.2 Determinism
Recovery must always produce:
- identical architecture  
- identical behaviour  
- identical reasoning environment  
- identical modelling outputs (given same values)  

### 3.3 Snapshot Consistency
All four layers must share:
- the same snapshot date  
- the same snapshot family  
- the same recovery manifest  

---

# 4. Validation Checklist

Before declaring recovery complete:

- [ ] Engine rebuilt and validated  
- [ ] Operational parameters loaded and validated  
- [ ] Business context loaded  
- [ ] Business values loaded  
- [ ] Derived views regenerated  
- [ ] No contradictions across layers  
- [ ] Governance intact  
- [ ] Invariants intact  
- [ ] Behaviour deterministic  

---

# 5. Summary
This protocol defines the **complete, deterministic, four-layer recovery process** for the Clarity Engine.  
When executed in order, it restores:

- the system  
- the assumptions  
- the reasoning  
- the numerical model  
- the worldview  

exactly as they existed at the snapshot date.

This ensures the Clarity Engine can always be **rebuilt, verified, and trusted**.
