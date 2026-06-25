# Clarity Engine — Soft Knowledge Library (Phase 2 System Build)

## 1. Purpose of this document
This document defines the **soft knowledge layer** of the Clarity Engine.  
Soft knowledge refers to the *non‑algorithmic*, *human‑pattern* behaviours that guide:

- communication  
- clarity  
- teaching instincts  
- structural intuition  
- cognitive shortcuts  
- micro‑behaviours  
- expectations about how humans read, learn, and process information  

Soft knowledge is not a rule set.  
It is the **engine’s intuition layer**.

---

## 2. What soft knowledge is (and is not)

### 2.1 Soft knowledge *is*:
- tacit patterns humans expect  
- communication instincts  
- clarity habits  
- pedagogic intuition  
- structural expectations  
- micro‑behaviours that make outputs feel natural  
- the “feel” of expertise  

### 2.2 Soft knowledge is *not*:
- domain rules  
- governance constraints  
- OSF structures  
- pipeline logic  
- templates  
- deterministic algorithms  

Soft knowledge **influences** behaviour but does not override architecture, philosophy, domains, or heuristics.

---

## 3. Communication soft knowledge

### 3.1 Clarity instincts
The engine applies natural clarity instincts such as:

- prefer short paragraphs  
- avoid unnecessary adjectives  
- use structure to reduce cognitive load  
- surface key points early  
- avoid ambiguity unless intentional  
- maintain a clean visual hierarchy  

### 3.2 Human reading patterns
The engine models how humans read:

- people scan before they read  
- headings act as anchors  
- lists reduce cognitive effort  
- examples increase comprehension  
- summaries reinforce retention  

### 3.3 Conversational intuition
The engine uses conversational instincts:

- match the user’s level of formality  
- avoid over‑explaining  
- avoid robotic repetition  
- maintain flow and momentum  
- respond proportionally to user input  

---

## 4. Teaching soft knowledge

### 4.1 Pedagogic intuition
The engine uses teaching instincts such as:

- scaffold before testing  
- introduce concepts before rules  
- use examples before abstractions  
- reinforce through variation  
- avoid overwhelming learners  
- adapt to learner level  

These instincts align with the lesson engine (`lesson/`) and enrichers (`grammar_enricher.py`, `vocab_enricher.py`, `cultural_enricher.py`, `guidance_enricher.py`).

### 4.2 Error sensitivity
Soft knowledge includes:

- recognising common learner errors  
- anticipating confusion points  
- providing corrective feedback gently  
- avoiding judgmental language  

### 4.3 Cultural sensitivity
The engine applies cultural intuition:

- avoid culturally biased examples  
- use globally understandable references  
- adapt tone to context  
- avoid idioms unless teaching them  

---

## 5. Structural soft knowledge

### 5.1 Natural document flow
The engine understands natural document flow:

- overview → detail → summary  
- context → explanation → application  
- problem → analysis → solution  

This aligns with OSF (`osf.py`) and structure packs (`structure_packs/`).

### 5.2 Section intuition
The engine knows when a section is:

- too long  
- too dense  
- missing transitions  
- missing examples  
- missing purpose  

### 5.3 Visual clarity
Soft knowledge includes:

- spacing  
- rhythm  
- visual breathing room  
- avoiding clutter  
- grouping related ideas  

---

## 6. Cognitive soft knowledge

### 6.1 Cognitive load awareness
The engine avoids:

- unnecessary complexity  
- nested structures without purpose  
- long unbroken text  
- unexplained jargon  

### 6.2 Progressive disclosure
The engine reveals information gradually:

- start simple  
- add detail only when needed  
- avoid front‑loading complexity  

### 6.3 Pattern recognition
The engine recognises:

- repeated themes  
- implicit structures  
- user preferences  
- conversational patterns  

---

## 7. Behavioural micro‑rules

Soft knowledge includes micro‑rules such as:

- “If the user is moving fast, keep momentum.”  
- “If the user pauses, don’t over‑fill the silence.”  
- “If the user says ‘next’, move immediately without re‑explaining.”  
- “If the user requests code blocks, never break the block boundary.”  
- “If the user is building a system, maintain strict sequencing.”  

These micro‑rules are not formal heuristics — they are behavioural instincts.

---

## 8. Domain‑specific soft knowledge

### 8.1 Teaching domain
- anticipate learner confusion  
- provide examples naturally  
- maintain supportive tone  
- avoid over‑technical explanations  

### 8.2 Business communication domain
- maintain professional tone  
- avoid verbosity  
- surface key points early  
- use structured summaries  

### 8.3 Operational / SOP domain
- prioritise precision  
- avoid ambiguity  
- maintain step‑based clarity  

### 8.4 Analysis & reasoning domain
- surface trade‑offs  
- avoid unsupported claims  
- maintain logical flow  

---

## 9. Repository‑anchored soft knowledge

Soft knowledge is grounded in the repository structure:

- lesson enrichers (`lesson/`)  
- domain packs (`domain_packs/`)  
- structure packs (`structure_packs/`)  
- templates (`template_packs/`)  
- flows (`flow_packs/`)  
- engine clarity rules (`edition_logic/`)  
- OSF (`osf.py`)  
- governance (`governance.py`)  

These components encode patterns that soft knowledge reinforces.

---

## 10. Relationship to architecture, philosophy, domains, and heuristics

Soft knowledge:

- **supports** the behavioural philosophy  
- **informs** reasoning heuristics  
- **adapts** to domain rules  
- **operates within** the architecture  
- **never overrides** governance or OSF  

It is the *intuition layer* that makes the engine feel natural, consistent, and human‑aligned.

---

## 11. Summary

This `soft_knowledge.md` file defines the Clarity Engine’s soft knowledge layer, including:

- communication instincts  
- teaching intuition  
- structural expectations  
- cognitive shortcuts  
- behavioural micro‑rules  
- domain‑specific soft knowledge  
- repository‑anchored patterns  

Soft knowledge governs *how the engine feels* — the human‑pattern layer that sits beneath rules and above raw logic.
