# Runtime Validation

Validation ensures that all outputs meet structural and semantic requirements.

## Types of Validation

- Structural validation  
- Field‑level validation  
- Cross‑field validation  
- Domain‑specific validation  

## Guarantees

- Deterministic outcomes  
- Edition‑consistent behaviour  
- Clear error reporting  
Validation
Validation ensures that the transformed, semantically meaningful data produced by the engine is correct, consistent, complete, and compliant with the rules defined by the selected edition and domain pack. It is the final gate before output, guaranteeing that the engine never produces invalid or contradictory results.

Validation is deterministic, edition‑aware, and conflict‑safe.

1. Purpose of Validation
Validation answers the question:

“Given the structured and transformed data, is it correct according to the rules of this edition?”

Validation ensures:

required fields are present

values are valid

constraints are respected

edition‑specific rules are enforced

contradictions are surfaced

the final output is safe and reliable

Validation is the engine’s quality and compliance layer.

2. Validation Types
2.1 Field Validation
Checks that individual fields are valid.

Examples:

start_date is a real date

priority is within allowed range

client.full_name is not empty

2.2 Structural Validation
Ensures the data model is complete and correctly shaped.

Examples:

project.timeline.start must exist if project.timeline.end exists

client.address must contain required subfields

2.3 Semantic Validation
Checks meaning and relationships between fields.

Examples:

start_date must be after sign_date

actual_offset_days ≤ max_start_offset_days

risk_score must match edition‑specific rules

2.4 Edition‑Specific Validation
Rules unique to an edition.

Examples:

Code
Healthcare edition:
  patient_age must be ≥ 0
  risk_level must match NHS scoring model

Enterprise edition:
  project_complexity_score must be computed and valid
Edition logic determines which validation rules apply.

3. Validation Order in the Pipeline
Validation runs after transforms and before output.

Pipeline sequence:

Input

Context

Edition resolution

Mappings

Transforms

Validation

Output

Validation is the final gate before the engine produces results.

4. Edition‑Aware Validation
Each edition may:

add validation rules

override validation rules

disable validation rules

extend validation rules

Edition logic resolves these using the edition chain:

Code
selected edition → parent → base
Child editions always take precedence.

5. Validation Conflicts
A conflict occurs when:

two editions define incompatible validation rules

a rule requires a field that another edition removes

two rules enforce contradictory constraints

semantic rules cannot be satisfied simultaneously

Conflicts must be surfaced, not ignored.

Important:  
A validation failure is not a conflict.
A conflict is edition‑level contradiction, not user‑level invalid data.

6. Validation Output
After validation runs, the engine produces:

a validation report

a list of errors (if any)

a list of warnings (optional)

a validated semantic model

a guarantee that the output is safe

If validation fails, the engine must:

stop

surface errors clearly

never produce partial or misleading output

7. Constraints
To ensure safety and determinism:

validation rules must be explicit

validation must not introduce ambiguity

validation must not depend on unmapped or untransformed fields

validation must be edition‑safe

all conflicts must be surfaced

validation must be deterministic and reproducible

Validation must always produce clear, actionable results.

8. Summary
Validation provides:

correctness

completeness

compliance

edition‑specific enforcement

semantic integrity

safe, reliable output

It is the engine’s final safeguard before producing results.