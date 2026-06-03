# Context Layer

The context layer converts raw input into a structured internal representation.

## Responsibilities

- Normalise text and metadata  
- Detect segments, blocks, and logical units  
- Prepare data for parsing  
- Maintain provenance and source references  

## Guarantees

- Deterministic segmentation  
- Stable identifiers  
- No domain‑specific logic at this stage  
Context
The Engine Context is the central state container used throughout the Clarity Engine’s execution pipeline. It holds all intermediate data, configuration, edition metadata, and runtime state required for deterministic, reproducible processing.

The context is immutable by default, with controlled mutation only through well‑defined pipeline stages.

1. Purpose of the Engine Context
The context answers the question:

“What does the engine know right now, and what state is required to continue execution?”

It ensures:

consistent state across all pipeline stages

isolation between steps

deterministic behaviour

edition‑aware execution

traceability and debugging support

The context is the single source of truth during execution.

2. Context Responsibilities
The context is responsible for:

storing the resolved edition

holding raw input

holding mapped fields

holding transformed semantic data

storing validation results

tracking errors

tracking pipeline progress

exposing metadata for tracing and debugging

The context must never:

perform business logic

apply transforms

apply validation rules

modify input data directly

infer missing values

It is a state container, not a logic layer.

3. Context Structure
The context contains several well‑defined sections:

3.1 Input
The raw input provided to the engine.

3.2 Edition
The resolved edition, including:

edition name

version

active rules

overrides

3.3 Mapped Data
The output of the mapping stage:

normalised fields

canonical names

resolved synonyms

3.4 Transformed Data
The semantic model produced by transforms:

derived fields

interpreted meaning

computed relationships

3.5 Validation State
Validation results, including:

field‑level validation

cross‑field validation

domain‑specific validation

warnings

errors

3.6 Runtime Metadata
Execution metadata, including:

timestamps

pipeline stage

trace IDs

debug flags

3.7 Errors
A structured list of errors encountered during execution.

4. Context Lifecycle
The context evolves through the pipeline in a controlled sequence:

Initialisation

Edition resolution

Mapping

Transforms

Validation

Serialization

Final output

Each stage receives a context and returns a new context with updated state.

This ensures:

immutability

predictability

safe error propagation

5. Edition‑Aware Behaviour
The context stores edition metadata so that:

mappings can be edition‑specific

transforms can be edition‑specific

validation rules can be edition‑specific

serialization can be edition‑specific

The context does not interpret edition rules — it only stores them.

6. Error Handling
The context tracks errors in a structured form:

error type

error code

message

offending field(s)

expected vs actual values

pipeline stage

If any error is present:

execution stops

no further stages run

the context is returned with error state

The context ensures safe, deterministic failure.

7. Traceability
The context integrates with the tracing system to provide:

step‑by‑step execution logs

intermediate state snapshots

edition metadata

timing information

error propagation paths

This enables deep debugging and reproducibility.

8. Constraints
To ensure safety and clarity:

the context must be immutable between stages

the context must not contain logic

the context must not infer missing data

the context must not modify input

the context must not depend on external state

the context must always be complete and self‑contained

The context must always represent a valid, coherent snapshot of engine state.

9. Summary
The Engine Context provides:

a unified state model

edition‑aware execution

deterministic pipeline behaviour

structured error tracking

deep traceability

a stable foundation for all runtime operations

It is the backbone of the Clarity Engine’s execution model.