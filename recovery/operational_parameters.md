# Operational Parameters — Clarity Engine (Phase 3)
Snapshot ID: OP-2026-06-25-01
Snapshot Date: 2026-06-25
Environment: Production
Edition/Domain: Clarity Engine (General)

Associated Business Context Snapshot: BC-2026-06-25-01  
Associated Business Values Snapshot: BV-2026-06-25-01  

---

## 1. Purpose
This document defines the **operational parameters** used by the Clarity Engine during:
- modelling  
- forecasting  
- lesson‑plan generation  
- business logic  
- scenario analysis  
- user‑facing outputs  

These parameters are **not** part of the system layer.  
They are **contextual, adjustable, and scenario‑dependent**.

---

## 2. Parameter Categories

### 2.1 Market & Adoption Parameters
These values represent **assumptions**, not system truths.

- **Global teacher population (assumed):** 12,000,000  
- **Online‑capable teachers (assumed):** 20%  
- **Adoption rate (baseline scenario):** 0.5%  
- **Adoption rate (optimistic scenario):** 1.5%  
- **Adoption rate (conservative scenario):** 0.2%  
- **Monthly churn assumption:** 3%  
- **Monthly organic growth:** 1.2%  

These numbers are **imaginary placeholders** until replaced by real data.

---

### 2.2 Pricing & Revenue Parameters
- **Average lesson price (global blended):** €18  
- **Platform fee assumption:** 15%  
- **Teacher retention uplift (with Clarity):** +8%  
- **Lesson‑prep time reduction:** 35%  
- **Teacher productivity uplift:** 12%  

---

### 2.3 Cost & Opex Parameters
- **Server cost per active teacher:** €0.42 / month  
- **Support cost per 1,000 teachers:** €180 / month  
- **AI inference cost per lesson:** €0.012  
- **Fixed monthly overhead:** €2,500  

---

### 2.4 Conversion Funnel Parameters
- **Landing → Signup:** 8%  
- **Signup → Active:** 22%  
- **Active → Paying:** 9%  
- **Paying → Retained (90‑day):** 72%  

---

### 2.5 Lesson Engine Parameters
These are **operational**, not structural.

- **Default lesson duration:** 60 minutes  
- **Warm‑up proportion:** 10%  
- **Controlled practice proportion:** 35%  
- **Freer practice proportion:** 35%  
- **Assessment proportion:** 20%  
- **Vocabulary target per lesson:** 8–12 items  
- **Error‑correction density:** medium  
- **Cultural note frequency:** 1–2 per lesson  

---

### 2.6 Edition Behaviour Parameters
These are **edition‑level operational assumptions**, not edition rules.

- **Trainer edition verbosity:** high  
- **Client edition verbosity:** medium  
- **Cultural edition enrichment:** high  
- **Composite edition density:** medium‑high  
- **Formatting strictness:** high  

Edition *rules* are defined in `edition_rules_full.md`.  
Edition *parameters* live here.

---

### 2.7 Scenario Parameters
These allow the engine to run different simulations.

#### Baseline scenario
- adoption: 0.5%  
- churn: 3%  
- growth: 1.2%  

#### Optimistic scenario
- adoption: 1.5%  
- churn: 2%  
- growth: 2.5%  

#### Conservative scenario
- adoption: 0.2%  
- churn: 4%  
- growth: 0.5%  

---

## 3. Parameter Governance

### 3.1 What parameters *are*
- adjustable  
- scenario‑dependent  
- user‑facing  
- non‑structural  
- non‑governing  

### 3.2 What parameters *are not*
- system rules  
- domain rules  
- edition rules  
- architecture  
- philosophy  
- governance  

Parameters **cannot** override system behaviour.

---

## 4. Update Rules
- Parameters may be updated at any time.  
- Updates must not contradict system‑layer documents.  
- Updates must be logged in the change register.  
- Updates must be validated against governance.  
- Updates must not introduce drift.  

---

## 5. Summary
This file defines the **operational assumptions** used by the Clarity Engine.  
These values are **contextual**, **replaceable**, and **scenario‑driven**.  
They do not affect the engine’s identity — only its **outputs**.
