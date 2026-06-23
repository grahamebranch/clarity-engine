# manual_pipeline_test.py
# Simple manual test harness for the RAMEON engine.

from rameon_engine import RameonEngine

engine = RameonEngine()

test_text = """
Clarity Engine is a system designed to improve structure, coherence,
and readability of text by applying a multi‑stage transformation pipeline.
"""

print("\n=== INPUT TEXT ===\n")
print(test_text)

print("\n=== RUNNING RAMEON PIPELINE ===\n")
result = engine.run(test_text)

print("\n=== OUTPUT TEXT ===\n")
print(result)
