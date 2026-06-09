"""
Manual Pipeline Test - v1.1

This script runs the full Clarity Engine pipeline end-to-end:
DIS → OSF → Rameon → Governance

It uses a tiny example domain and structure so you can confirm
that the engine layers connect and behave deterministically.
"""

from engine_layer.dis import DIS
from engine_layer.osf import OSF
from engine_layer.rameon import RameonEngine
from engine_layer.governance import Governance


def run_manual_pipeline_test():
    # ---------------------------------------------------------
    # 1. Create engine layer instances
    # ---------------------------------------------------------
    dis = DIS()
    osf = OSF()
    rameon = RameonEngine()
    gov = Governance()

    # ---------------------------------------------------------
    # 2. Register a tiny example domain
    # ---------------------------------------------------------
    example_domain = {
        "name": "example",
        "flows": {"flow1": "do something"},
        "templates": {"template1": "example template"},
        "constraints": {"max_length": 200},
        "annex_rules": {"rule1": "annex behaviour"},
    }

    dis.register_domain("example", example_domain)

    # ---------------------------------------------------------
    # 3. Register a tiny OSF structure
    # ---------------------------------------------------------
    example_structure = {
        "sections": ["intro", "body", "summary"]
    }

    osf.register_structure("example", "v1", example_structure)

    # ---------------------------------------------------------
    # 4. Load domain + structure
    # ---------------------------------------------------------
    domain_rules = dis.load_domain("example")
    structure = osf.load_structure("example", "v1")

    # ---------------------------------------------------------
    # 5. Run DIS
    # ---------------------------------------------------------
    instruction_set = dis.interpret(
        user_request="Write something simple.",
        domain_rules=domain_rules
    )

    # ---------------------------------------------------------
    # 6. Run OSF
    # ---------------------------------------------------------
    shaped_output = osf.apply_structure(
        instruction_set=instruction_set,
        structure=structure
    )

    # ---------------------------------------------------------
    # 7. Run Rameon
    # ---------------------------------------------------------
    executed_output = rameon.execute(
        instruction_set=instruction_set,
        structure=structure,
        domain_rules=domain_rules
    )

    # ---------------------------------------------------------
    # 8. Run Governance validations
    # ---------------------------------------------------------
    domain_check = gov.validate_domain("example", instruction_set)
    edition_check = gov.validate_edition("v1", {"edition": "v1"})
    structure_check = gov.validate_structure(structure, executed_output)
    constraint_check = gov.validate_constraints(domain_rules, executed_output)

    # ---------------------------------------------------------
    # 9. Return everything for inspection
    # ---------------------------------------------------------
    return {
        "instruction_set": instruction_set,
        "shaped_output": shaped_output,
        "executed_output": executed_output,
        "domain_check": domain_check,
        "edition_check": edition_check,
        "structure_check": structure_check,
        "constraint_check": constraint_check,
    }


if __name__ == "__main__":
    result = run_manual_pipeline_test()
    print("\n=== MANUAL PIPELINE TEST RESULT ===\n")
    for key, value in result.items():
        print(f"{key.upper()}:\n{value}\n")
