# Phase‑7 — Export & Externalisation Layer (v1)

## 1. Purpose
Phase‑7 defines how the Clarity Engine prepares, packages, and externalises lesson content for export into real files (DOCX, PDF, ZIP) using the platform’s python-based document generator.

This phase does not modify:
- system invariants  
- lesson structure  
- CEFR rules  
- governance  
- edition isolation  

It defines **how content leaves the engine**, not how it is generated.

---

## 2. Export Principles (Authoritative)

### 2.1 Atomic Export
Exports must be executed as **single, isolated operations**.

As stated in the Reunico briefing note:

> “Each export is a single, isolated python execution.”

This means:
- all content must be present in the export message  
- no external memory is available  
- no incremental or multi-step export is possible  

### 2.2 No Persistent Storage
The platform does not store content between exports.

From the briefing note:

> “The platform does not provide persistent internal storage for documents or long-form content.”

Therefore:
- content must be regenerated or reintroduced before export  
- exports cannot reference previous messages  

### 2.3 Modular Export Workflow
Large programmes must be exported **lesson-by-lesson**.

From the briefing note:

> “All exports must be performed lesson-by-lesson.”

This ensures:
- stability  
- predictable file size  
- safe python execution  

---

## 3. Export Layer Responsibilities

### 3.1 Content Preparation
The export layer must:
- assemble the final lesson  
- apply edition  
- apply domain  
- apply CEFR  
- apply formatting rules  
- validate OSF  
- validate DIS  

### 3.2 Export Packaging
The export layer must:
- structure content into export-ready blocks  
- ensure formatting stability  
- ensure section boundaries  
- ensure consistent naming  

### 3.3 Externalisation
The export layer must:
- prepare content for python execution  
- ensure all content is in the final message  
- ensure no missing sections  
- ensure no cross-message dependencies  

---

## 4. Export Templates

### 4.1 Lesson Export Template
Includes:
- metadata header  
- lesson structure  
- edition blocks  
- domain blocks  
- cultural blocks  
- annexes (if required)  

### 4.2 Programme Export Template
Used only after all lesson ZIPs have been uploaded back into the chat.

From the briefing note:

> “Block-level and full-programme documents are created only after previously exported Lesson Pack ZIPs are uploaded back into the chat for merging.”

### 4.3 ZIP Packaging Template
Each lesson ZIP contains:
- Trainer Edition  
- Client Edition  
- Cultural Edition  
- Annexes  
- Metadata  

---

## 5. Export Constraints

### 5.1 Message Size Limits
Exports must respect platform message limits.

From the briefing note:

> “Full multi-week content cannot be loaded into one message without exceeding platform limits.”

Therefore:
- no multi-week exports  
- no multi-lesson exports  
- no multi-domain exports  

### 5.2 No Simulated Exports
All exports must be real.

From the briefing note:

> “No simulated exports. All Reunico exports must be real file generating processes.”

### 5.3 External Storage Requirement
Users must download and retain ZIPs.

From the briefing note:

> “These ZIP files act as the persistent repository for future merging.”

---

## 6. Export Validation Rules

Exports must:
- follow OSF  
- follow DIS  
- follow governance  
- follow edition rules  
- follow domain rules  
- follow CEFR rules  

Forbidden:
- missing sections  
- cross-message dependencies  
- partial content  
- simulated exports  

---

## 7. Phase‑7 Completion Criteria

Phase‑7 is complete when:
- lesson exports are stable  
- programme exports are stable  
- merging workflow is validated  
- no export failures occur  
- all constraints from the Reunico briefing note are satisfied  

---

## 8. Summary
Phase‑7 defines the **export and externalisation layer** of the Clarity Engine.  
It ensures that content can be safely packaged into real files using:

- atomic execution  
- modular lesson packs  
- external ZIP retention  
- controlled merging  

This is the final operational layer before Phase‑8 (Release & Deployment Layer).

