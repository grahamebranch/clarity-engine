# Phase‑13 — Canonical Test Suite (v1)

## 1. Purpose
Phase‑13 defines the behavioural tests required to confirm that a rebuilt Clarity Engine (via Phase‑12) is functioning correctly.

These tests ensure:
- structural correctness  
- semantic correctness  
- governance compliance  
- edition/domain isolation  
- runtime stability  
- export stability  

---

## 2. Test Categories

### 2.1 Structural Tests
Verify:
- lesson structure  
- section ordering  
- formatting invariants  
- CEFR alignment  

### 2.2 Semantic Tests
Verify:
- tone correctness  
- register correctness  
- meaning preservation  
- edition/domain isolation  

### 2.3 Governance Tests
Verify:
- OSF compliance  
- DIS compliance  
- forbidden content filters  
- safety rules  

### 2.4 Runtime Tests
Verify:
- routing  
- transformation pipeline  
- sequencing  
- reproducibility  

### 2.5 Export Tests
Verify:
- atomic export behaviour  
- correct packaging  
- no cross‑message dependencies  

---

## 3. Test Templates

### 3.1 Structural Test Template
1. Generate lesson  
2. Validate structure  
3. Validate CEFR  
4. Validate formatting  

### 3.2 Semantic Test Template
1. Generate lesson  
2. Apply Edition A  
3. Apply Edition B  
4. Compare outputs  
5. Validate isolation  

### 3.3 Governance Test Template
1. Generate lesson  
2. Scan for violations  
3. Validate OSF  
4. Validate DIS  

### 3.4 Runtime Test Template
1. Generate lesson  
2. Apply transformations  
3. Validate routing  
4. Validate reproducibility  

### 3.5 Export Test Template
1. Generate lesson  
2. Prepare export  
3. Validate atomicity  
4. Validate completeness  

---

## 4. Test Execution Rules

- Tests must be run after every recovery  
- Tests must be run after every update  
- Tests must be deterministic  
- Tests must not modify the engine  
- Tests must not introduce drift  

---

## 5. Completion Criteria

Phase‑13 is complete when:
- all tests pass  
- no drift detected  
- no violations detected  
- runtime behaviour matches baseline  
- export behaviour matches baseline  

---

## 6. Summary
Phase‑13 defines the canonical behavioural test suite for the Clarity Engine.  
It ensures that any rebuilt or updated engine behaves exactly as intended.
