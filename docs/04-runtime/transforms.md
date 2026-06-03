Transforms
Transforms define how the Clarity Engine converts clean, structured input (produced by mappings) into semantically meaningful, edition‑aware data. They interpret meaning, derive new values, restructure objects, and prepare the data for validation and output.

Transforms are where the engine becomes intelligent — moving from “what the user said” to “what the requirement actually means”.

1. Purpose of Transforms
Transforms answer the question:

“Given structured input, what does this mean in the context of the selected edition?”

Transforms can:

split a single requirement into multiple components

merge multiple fields into one

derive new values

compute metrics

interpret semantics

apply edition‑specific logic

prepare data for validation

They operate on the canonical data produced by mappings.

2. Transform Types
2.1 Structural Transforms
Reshape the structure of the data.

Examples:

Code
client.full_name → client.name.first + client.name.last
address → location.address
These ensure the data model matches the domain pack’s expected structure.

2.2 Semantic Transforms
Interpret meaning from structured input.

Example:

Code
"must start within 30 days" → max_start_offset_days = 30
These convert human‑expressed constraints into machine‑readable semantics.

2.3 Derived Transforms
Compute new values based on existing fields.

Examples:

Code
actual_offset_days = start_date - sign_date
risk_score = age_factor + condition_factor
These enrich the data with computed insights.

2.4 Edition‑Specific Transforms
Apply logic unique to an edition.

Examples:

Code
Healthcare edition:
  derive patient_risk_level

Enterprise edition:
  derive project_complexity_score
Edition logic determines which transforms apply.

3. Transform Order in the Pipeline
Transforms run after mappings and before validation.

Pipeline sequence:

Input

Context

Edition resolution

Mappings

Transforms

Validation

Output

Transforms prepare the data for validation and output.

4. Edition‑Aware Transforms
Each edition may:

add transforms

override transforms

disable transforms

extend transforms

Edition logic resolves these using the edition chain:

Code
selected edition → parent → base
Child editions always take precedence.

5. Transform Conflicts
A conflict occurs when:

two editions define incompatible transforms

a transform depends on a field removed by another edition

two transforms produce contradictory derived values

transforms create incompatible shapes

Conflicts must be surfaced, not ignored.

Important:  
Splitting a requirement into multiple components is not a conflict.
Deriving new fields is not a conflict.
Normalising or interpreting meaning is not a conflict.

Conflicts arise only from edition‑level contradictions.

6. Transform Output
After transforms run, the engine produces:

structured data

derived fields

semantic interpretations

edition‑specific enrichments

computed values

ready‑to‑validate objects

This is the semantic model of the input.

7. Constraints
To ensure safety and determinism:

transforms must be explicit

transforms must not introduce ambiguity

transforms must not create circular dependencies

transforms must be edition‑safe

all conflicts must be surfaced

transforms must operate only on mapped, canonical data

Transforms must always produce valid, semantically meaningful structures.

8. Summary
Transforms provide:

semantic understanding

edition‑specific behaviour

derived insights

structured meaning

clean input for validation

predictable, deterministic behaviour

They are the engine’s bridge between clean input and validated, meaningful output.