Mappings
Mappings define how the Clarity Engine converts messy, inconsistent, human‑written input into clean, structured, predictable data that downstream components can rely on. They are the first transformation step after edition resolution and form the foundation for transforms, validation, and output.

Mappings are edition‑aware, deterministic, and conflict‑safe.

1. Purpose of Mappings
Mappings answer one question:

“How do we turn whatever the user wrote into the structured fields the engine expects?”

They handle:

inconsistent naming

cultural differences (e.g., dates)

synonyms

alternative phrasings

structural differences

type conversions

normalisation

splitting or merging fields

Mappings ensure the engine always receives clean, canonical input, regardless of how the user expresses it.

2. Mapping Types
Mappings fall into three categories:

2.1 Field Mappings
Rename or redirect fields.

Examples:

Code
"customer name" → client.full_name
"start date" → project.timeline.start
These resolve synonyms and inconsistent terminology.

2.2 Structural Mappings
Move or reshape data.

Examples:

Code
address.line1 → location.address.street
contact → client.primary_contact
These ensure the engine receives data in the correct structure.

2.3 Transformational Mappings
Convert or normalise values.

Examples:

Code
"yes" → true
"01/02/2025" → 2025-02-01 (ISO)
"high" → priority:3
These handle cultural differences, formats, and type conversions.

3. Mapping Order in the Pipeline
Mappings run after edition resolution and before transforms.

Pipeline sequence:

Input

Context

Edition resolution

Mappings

Transforms

Validation

Output

This ensures transforms and validation operate on clean, structured data, not raw input.

4. Edition‑Aware Mappings
Each edition may:

add mappings

override mappings

disable mappings

extend mappings

Example:

Code
base edition:
  "customer name" → client.full_name

healthcare edition:
  "patient name" → client.full_name
The engine resolves these using the edition chain:

Code
selected edition → parent → base
Child editions always take precedence.

5. Mapping Conflicts
A conflict occurs only when two editions define incompatible mappings for the same input.

Examples:

Base: "start date" → ISO date

Healthcare: "start date" → DD/MM/YYYY

NHS: "start date" → MM/DD/YYYY

These cannot be merged and must be surfaced.

Important:  
Splitting a messy requirement into multiple structured fields is not a conflict.
Normalising dates or formats is not a conflict.
Cultural differences are handled through transformational mappings, not conflict logic.

Conflicts arise only from edition‑level contradictions.

6. Mapping Output
After mappings run, the engine produces:

a clean, canonical object

with predictable field names

consistent types

normalised formats

edition‑specific behaviour applied

This output is the input to transforms and validation.

7. Constraints
To ensure safety and determinism:

Mappings must be explicit

Mappings must not introduce ambiguity

Mappings must not create circular references

All mapping overrides must be edition‑safe

All conflicts must be surfaced, not ignored

Mappings must always produce valid, structured data.

8. Summary
Mappings provide:

consistency across messy input

edition‑specific behaviour

predictable structure

clean data for transforms and validation

safe conflict detection

They are the engine’s first line of defence against ambiguity and inconsistency.