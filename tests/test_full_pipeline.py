"""
Full Pipeline Sanity Test - Checkpoint 7 (Debug Version)

This test verifies:
- OSF shaping
- EL3 structural normalisation
- EL4 clarity edits
- EL5 rewrite tightening
- Governance safety
- FinalOutput cleanup
- RameonEngine orchestration

Run with:
    python tests/test_full_pipeline.py
"""

import sys
import os

# Ensure project root is on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from rameon_engine import RameonEngine


def run_full_pipeline_test():
    engine = RameonEngine()

    test_input = """
We might possibly need to make a decision, however it is not ideal at this point in time.
There is a need to give consideration to the options, but it should probably wait.

- item one
- item two

In order to ensure clarity, it is important to note that we should probably begin soon.
"""

    print("\n==============================")
    print(" FULL PIPELINE SANITY TEST")
    print("==============================\n")

    print(">>> INPUT TEXT:")
    print(test_input)

    print("\n>>> DEBUG: OSF OUTPUT:")
    osf_out = engine.osf.osf(test_input)
    print(osf_out)

    print("\n>>> DEBUG: EL3 OUTPUT:")
    el3_out = engine.el3.el3(osf_out)
    print(el3_out)

    print("\n>>> DEBUG: EL4 OUTPUT:")
    el4_out = engine.el4.el4(el3_out)
    print(el4_out)

    print("\n>>> DEBUG: EL5 OUTPUT:")
    el5_out = engine.el5.el5(el4_out)
    print(el5_out)

    print("\n>>> DEBUG: GOVERNANCE OUTPUT:")
    gov_out = engine.gov.governance(el5_out)
    print(gov_out)

    print("\n>>> DEBUG: FINAL OUTPUT LAYER:")
    final_out = engine.final.final_output(gov_out)
    print(final_out)

    print("\n>>> DEBUG: FULL ENGINE OUTPUT:")
    full_out = engine.process(test_input)
    print(full_out)

    print("\n==============================")
    print(" END OF TEST")
    print("==============================\n")


if __name__ == "__main__":
    run_full_pipeline_test()
