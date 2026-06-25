# Clarity Engine — Full Interfaces Model (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **interfaces layer** of the Clarity Engine.  
Interfaces govern how the engine:

- exposes itself to external systems  
- receives requests  
- returns structured outputs  
- integrates with UI, CLI, API, and adapters  
- maintains clarity and determinism at the boundary  

Interfaces are the **entry and exit points** of the system.

---

## 2. What interfaces are

### 2.1 Interfaces *are*:
- API endpoints  
- CLI commands  
- adapters  
- UI integration points  
- server routing  
- external‑facing contracts  

### 2.2 Interfaces are *not*:
- domain logic  
- templates  
- flows  
- OSF or DIS  
- governance rules  
- runtime logic  

Interfaces **expose** the engine; they do not **implement** it.

---

## 3. Interface components

Interfaces are implemented in:

- `src/api/`  
- `src/cli/`  
- `src/adapters/`  
- `src/services/`  
- `server.py`  
- `ui/`  
- `docs/05-interfaces/` (API, CLI, adapters, formats)  

These components define how external systems interact with the engine.

---

## 4. API Interface

### 4.1 Purpose
The API exposes the engine to external systems via structured requests.

### 4.2 Location
- `src/api/`  
- `docs/05-interfaces/api.md`  
- `server.py`  

### 4.3 Responsibilities
- accept structured JSON requests  
- validate inputs  
- route to engine  
- return deterministic outputs  
- provide trace and error metadata  

### 4.4 API contract
The API contract includes:

- `input_text`  
- `mode` (domain)  
- `edition`  
- `options`  
- `metadata`  

### 4.5 Behaviour
The API must:

- be stable  
- be deterministic  
- be backward compatible  
- return structured JSON  
- include trace metadata when requested  

---

## 5. CLI Interface

### 5.1 Purpose
The CLI provides a developer‑friendly interface for interacting with the engine.

### 5.2 Location
- `src/cli/`  
- `docs/05-interfaces/cli.md`  

### 5.3 Responsibilities
- accept files and stdin  
- validate inputs  
- run the pipeline  
- display results and traces  
- support scripting and automation  

### 5.4 Requirements
- stable commands and flags  
- clear exit codes  
- machine‑readable output options  
- edition‑aware behaviour  

---

## 6. Adapters Interface

### 6.1 Purpose
Adapters integrate the engine with external systems and transports.

### 6.2 Location
- `src/adapters/`  
- `docs/05-interfaces/adapters.md`  

### 6.3 Responsibilities
- translate external protocols into API requests  
- handle authentication and routing  
- manage retries and timeouts  
- capture traces and errors  

### 6.4 Adapter types
- HTTP adapters  
- message queue adapters  
- file‑based adapters  
- custom integration adapters  

---

## 7. UI Interface

### 7.1 Purpose
The UI exposes the engine to end‑users via a browser interface.

### 7.2 Location
- `ui/`  
- `server.py` (serves UI)  

### 7.3 Responsibilities
- accept user input  
- send structured requests to API  
- display formatted output  
- maintain clarity and structure  
- support lesson generation and testing  

### 7.4 UI components
- `ui.js`  
- `dashboard.html`  
- `index.html`  
- `script.js`  
- `style.css`  

### 7.5 UI constraints
- must not implement business logic  
- must not bypass API  
- must not alter engine output  
- must preserve formatting  

---

## 8. Server Interface

### 8.1 Purpose
`server.py` acts as the bridge between:

- API  
- UI  
- engine  

### 8.2 Responsibilities
- route requests  
- validate payloads  
- call engine  
- return structured responses  
- handle errors gracefully  

### 8.3 Behaviour
The server must:

- be stateless  
- be deterministic  
- avoid caching engine outputs  
- log errors for diagnostics  

---

## 9. Interface governance

Interfaces must comply with:

- domain boundaries  
- edition rules  
- OSF  
- DIS  
- governance constraints  
- runtime validation  

Interfaces **cannot** override:

- structure  
- domain rules  
- edition logic  
- safety rules  

Interfaces **must** preserve:

- clarity  
- determinism  
- structure  
- metadata  

---

## 10. Interface clarity rules

Interfaces must follow clarity rules:

- clear parameter names  
- predictable response structure  
- consistent error messages  
- stable endpoints  
- no hidden behaviour  

---

## 11. Interface error handling

Interfaces must:

- validate inputs  
- reject malformed requests  
- return structured error objects  
- include trace metadata when available  
- avoid leaking internal stack traces  

---

## 12. Repository‑anchored interface model

Interfaces are grounded in:

- `src/api/`  
- `src/cli/`  
- `src/adapters/`  
- `src/services/`  
- `server.py`  
- `ui/`  
- `docs/05-interfaces/`  

These components define the authoritative interface behaviour.

---

## 13. Relationship to architecture, philosophy, domains, heuristics, soft knowledge, business knowledge, workflow knowledge, governance, and runtime

Interfaces:

- **expose** the architecture  
- **express** the philosophy at the boundary  
- **respect** domain and edition rules  
- **use** heuristics and soft knowledge indirectly  
- **execute** workflows via API and CLI  
- **obey** governance  
- **run** within the runtime lifecycle  

Interfaces are the **controlled boundary** between the engine and the outside world.

---

## 14. Summary

This `interfaces_full.md` file defines the Clarity Engine’s interface layer, including:

- API  
- CLI  
- adapters  
- UI  
- server routing  
- interface governance  
- clarity rules  
- error handling  
- repository‑anchored interface components  

Interfaces govern *how the engine communicates with external systems and users*.
