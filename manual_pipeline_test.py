# ============================================================
# Manual Pipeline Test — EL3 Deterministic Pass
# ============================================================

from engine_layer.rameon import RameonEngine

engine = RameonEngine()

test_text = """
We are going to resolve it slightly later. It is suboptimal but we will resolve the matter.
I think we require to commence the process and provide people time to respond.
In order to ensure clarity we should utilise a better structure however it might not be necessary.
The team will begin soon.
"""

result = engine.run(test_text)

print("\n=== EL3 TEST INPUT ===\n")
print(test_text.strip())

print("\n=== EL3 TEST OUTPUT ===\n")
print(result.strip())
