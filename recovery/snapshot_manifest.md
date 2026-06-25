# Snapshot Manifest — Clarity Engine
Snapshot Family: 2026-06-25  
Environment: Production

This manifest lists all canonical files required for a **full deterministic rebuild** of the Clarity Engine at the snapshot date.

---

# 1. Engine Layer (Canonical)
Snapshot ID: ENG-2026-06-25-01  
Files:
- phase_01_foundations.md  
- phase_02_architecture.md  
- phase_03_invariants.md  
- phase_04_governance.md  
- phase_05_runtime.md  
- phase_06_export.md  
- phase_07_lifecycle.md  
- phase_08_validation.md  
- phase_09_testing.md  
- phase_10_audit.md  
- phase_11_lockdown.md  
- phase_12_maintenance.md  
- phase_13_canonical_test_suite_v1.md  
- phase_14_integrations.md  
- phase_15_editions.md  
- phase_16_scenarios.md  
- phase_17_extensions.md  
- phase_18_final_checks.md  

All engine files must be loaded in order.

---

# 2. Operational Parameters Layer
Snapshot ID: OP-2026-06-25-01  
File:
- operational_parameters.md  

Purpose:
- adoption assumptions  
- pricing assumptions  
- cost assumptions  
- lesson engine operational settings  
- edition behaviour parameters  
- scenario definitions  

---

# 3. Business Context Layer
Snapshot ID: BC-2026-06-25-01  
File:
- business_context.md  

Purpose:
- strategic intent  
- worldview  
- decision logic  
- human values  
- reasoning environment  
- historical decisions  
- risk posture  
- market understanding  

---

# 4. Business Values Layer
Snapshot ID: BV-2026-06-25-01  
File:
- business_values.md  

Purpose:
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

---

# 5. Recovery Protocol
Snapshot ID: REC-2026-06-25-01  
File:
- recovery_protocol.md  

Purpose:
- authoritative rebuild sequence  
- validation rules  
- integrity rules  
- deterministic behaviour guarantees  

---

# 6. Completeness
All files listed above are required for a **full deterministic rebuild**.  
Missing any layer results in an incomplete or non‑deterministic recovery.

This manifest is the **top‑level index** for the entire recovery pack.
