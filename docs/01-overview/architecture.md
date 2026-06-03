===== docs/01-overview/architecture.md =====
# Clarity Engine — High‑Level Architecture

The Clarity Engine transforms messy, ambiguous, multi‑format input into structured, validated, traceable output.  
It does this through a layered, rule‑driven architecture designed for:

- determinism  
- auditability  
- domain isolation  
- versioned evolution  
- cross‑industry applicability  

## Core Layers

### 1. Input Context Layer  
Normalises raw input into a unified internal representation.

### 2. Pipeline Layer  
Orchestrates the full transformation lifecycle: parsing → resolving → mapping → validation → output.

### 3. Domain Packs  
Plug‑in modules that define domain‑specific rules, vocabularies, constraints, and mappings.

### 4. Edition Logic  
Versioned rule‑sets that ensure stability across releases and prevent drift.

### 5. Runtime Layer  
Executes transformations deterministically, with full traceability.

### 6. Interfaces Layer  
API, CLI, and adapters for external systems.
