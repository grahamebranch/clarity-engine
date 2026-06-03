# Pipeline

The pipeline defines the ordered sequence of stages that the Clarity Engine executes to transform raw input into a validated, edition‑aware semantic model. It provides the structural backbone of the engine’s behaviour and ensures deterministic, reproducible processing.

The pipeline is architectural — it describes what happens and in what order, not how each step is implemented.

---

## 1. Purpose of the pipeline

The pipeline answers the question:

> “What are the mandatory stages the engine must run, and how do they connect?”

It ensures:

- **consistent execution model**
- **strict ordering of stages**
- **edition‑aware behaviour**
- **predictable state transitions**
- **clean separation of responsibilities**
- **deterministic outcomes**

The pipeline is the skeleton of the engine.

---

## 2. Pipeline stages

The pipeline consists of the following ordered stages:

1. **Initialisation**  
2. **Edition Resolution**  
3. **Mapping**  
4. **Transforming**  
5. **Validation**  
6. **Serialization**  
7. **Final Output**

Each stage receives:

- the current **Engine Context**
- the **resolved edition**
- the **output of the previous stage**

And returns a **new context** with updated state.

---

## 3. Stage responsibilities

### 3.1 Initialisation

Creates the initial Engine Context:

- loads configuration  
- stores raw input  
- prepares runtime metadata  
- sets initial pipeline state  

No interpretation occurs here.

---

### 3.2 Edition Resolution

Determines which edition rules apply:

- resolves edition name and version  
- loads edition‑specific rules  
- loads overrides  
- prepares edition metadata  

Edition resolution must complete before any other stage runs.

---

### 3.3 Mapping

Normalises raw input into canonical fields:

- resolves synonyms  
- applies edition‑specific mapping rules  
- enforces field naming conventions  
- prepares data for transforms  

Mapping must not infer meaning — it only normalises structure.

---

### 3.4 Transforming

Builds the semantic model:

- derives new fields  
- interprets meaning  
- computes relationships  
- applies edition‑specific transform rules  

Transforms must not validate — they only interpret.

---

### 3.5 Validation

Ensures the semantic model is correct:

- structural validation  
- field‑level validation  
- cross‑field validation  
- domain‑specific validation  
- edition‑specific validation  

Validation must not modify data — it only checks correctness.

---

### 3.6 Serialization

Converts the validated model into output formats:

- JSON  
- YAML  
- Markdown  
- text  
- edition‑specific formats  

Serialization must not change meaning — only representation.

---

### 3.7 Final Output

Produces the final engine result:

- serialized output  
- metadata  
- trace information  
- error state (if any)  

This is the boundary between the engine and external systems.

---

## 4. Deterministic ordering

The pipeline is strictly linear:

- no skipping stages  
- no reordering  
- no loops  
- no recursion  
- no dynamic branching  

This ensures:

- reproducibility  
- testability  
- predictable behaviour  
- edition‑safe execution  

---

## 5. Interaction with the Engine Context

Each stage:

- reads from the context  
- writes to a **new** context  
- never mutates previous state  
- never depends on external global state  

This immutability ensures:

- clean debugging  
- safe error propagation  
- consistent state snapshots  
- reliable tracing  

---

## 6. Error propagation

If any stage produces an error:

- the pipeline stops immediately  
- no further stages run  
- the context is returned with error state  
- the error is wrapped with edition metadata  

No partial output is allowed.

---

## 7. Edition‑aware behaviour

Edition logic influences:

- mapping rules  
- transform rules  
- validation rules  
- serialization rules  

But:

> **The pipeline structure never changes.  
> Only the behaviour inside each stage changes.**

This preserves stability across editions.

---

## 8. Constraints

To ensure safety and clarity:

- stages must be pure  
- stages must not modify input  
- stages must not infer missing data  
- stages must not depend on external state  
- stages must not perform work belonging to another stage  

Each stage has a single, clear responsibility.

---

## 9. Summary

The pipeline provides:

- a deterministic execution model  
- strict stage ordering  
- edition‑aware behaviour  
- clean separation of concerns  
- safe error propagation  
- a stable foundation for runtime execution  

It is the architectural backbone of the Clarity Engine.
