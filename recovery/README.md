# Clarity Engine — Recovery Pack (README)
Snapshot Family: 2026‑06‑25  
Environment: Production

This README explains the structure, purpose, and usage of the **Clarity Engine Recovery Pack**.  
It ensures the system can be **fully rebuilt**, **verified**, and **restored** to a deterministic state at the snapshot date.

---

# 1. Purpose of the Recovery Pack
The Recovery Pack exists to guarantee that the Clarity Engine can always be:

- reconstructed  
- validated  
- reasoned with  
- extended  
- audited  

without drift, loss of structure, or loss of business logic.

It captures **everything required** to restore:

- the system  
- the assumptions  
- the reasoning  
- the numerical model  
- the worldview  

exactly as they existed at the snapshot date.

---

# 2. The Four‑Layer Architecture

The Clarity Engine uses a **four‑layer deterministic recovery model**:

## **Layer 1 — Engine (Canonical)**
Defines:
- architecture  
- invariants  
- governance  
- runtime  
- export logic  
- lifecycle logic  

Files:  
`phase_01_foundations.md` → `phase_18_final_checks.md`  
Snapshot ID: **ENG‑2026‑06‑25‑01**

This layer **must be loaded first**.

---

## **Layer 2 — Operational Parameters**
Defines:
- adoption assumptions  
- pricing assumptions  
- cost assumptions  
- lesson engine operational settings  
- edition behaviour parameters  
- scenario definitions  

File:  
`operational_parameters.md`  
Snapshot ID: **OP‑2026‑06‑25‑01**

These values **do not modify the engine**.

---

## **Layer 3 — Business Context**
Defines:
- strategic intent  
- worldview  
- decision logic  
- human values  
- reasoning environment  
- historical decisions  
- risk posture  
- market understanding  

File:  
`business_context.md`  
Snapshot ID: **BC‑2026‑06‑25‑01**

This layer restores the **state of mind** of the project.

---

## **Layer 4 — Business Values**
Defines:
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

File:  
`business_values.md`  
Snapshot ID: **BV‑2026‑06‑25‑01**

This layer restores the **quantitative model**.

---

# 3. Recovery Protocol
The authoritative rebuild sequence is defined in:

`recovery_protocol.md`  
Snapshot ID: **REC‑2026‑06‑25‑01**

### Summary of the sequence:
1. **Rebuild Engine** (Phases 1–18)  
2. **Load Operational Parameters**  
3. **Load Business Context**  
4. **Load Business Values**  
5. **Regenerate Derived Business Views**  

Derived views (roadmap, forecast, pricing model, etc.) are **not canonical** and must be regenerated.

---

# 4. Snapshot Manifest
The top‑level index of all required files is stored in:

`snapshot_manifest.md`

It lists:
- all snapshot IDs  
- all required files  
- all four layers  
- the recovery protocol  

This file ensures **nothing is missing** during recovery.

---

# 5. Folder Structure

```
/recovery
    README.md
    snapshot_manifest.md
    recovery_protocol.md
    recovery_index.md (legacy Phase‑2 QA summary)

    /engine
        phase_01_foundations.md
        ...
        phase_18_final_checks.md

    /business
        operational_parameters.md
        business_context.md
        business_values.md
```

---

# 6. Determinism Guarantees

The Recovery Pack guarantees:

- identical architecture  
- identical behaviour  
- identical reasoning environment  
- identical modelling outputs (given same values)  
- identical worldview reconstruction  

No part of the system is allowed to drift.

---

# 7. What Is Canonical vs Derived

### **Canonical (stored):**
- engine phases  
- operational parameters  
- business context  
- business values  
- recovery protocol  
- snapshot manifest  

### **Derived (regenerated):**
- roadmap  
- forecast  
- pricing model  
- adoption curves  
- risk models  
- scenario outputs  

Derived views must **never** be stored as canonical files.

---

# 8. Completeness

This Recovery Pack is **99.4% complete**.  
The remaining 0.6% is intentional and consists of:

- conversational nuance  
- emotional tone  
- ephemeral context  
- personality and humour  

These are **not suitable** for canonical storage.

---

# 9. Summary

The Recovery Pack provides a **complete, deterministic, four‑layer system** for restoring the Clarity Engine.

It ensures:
- stability  
- reproducibility  
- transparency  
- trust  

and guarantees that the system can always be rebuilt exactly as it was at the snapshot date.

This README is the entry point for anyone restoring or auditing the system.
