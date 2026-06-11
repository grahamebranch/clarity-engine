"""
Manual Pipeline Test - v1.2

Runs the full Clarity Engine pipeline end-to-end:
DIS → OSF → Rameon → Governance

Now using the real Teaching Domain Pack.
"""

from engine_layer.dis import DIS
from engine_layer.osf import OSF
from engine_layer.rameon import RameonEngine
from engine_layer.governance import Governance
from structure_packs.teaching_structure import get_teaching_structure
from template_packs.teaching_templates import get_teaching_templates
from flow_packs.teaching_flow import get_teaching_flow_logic



# Import your real domain pack
from domain_packs.teaching_domain import get_domain


def run_manual_pipeline_test():
    # ---------------------------------------------------------
    # 1. Create engine layer instances
    # ---------------------------------------------------------
    dis = DIS()
    osf = OSF()
    rameon = RameonEngine()
    gov = Governance()

    # ---------------------------------------------------------
    # 2. Register the real Teaching Domain
    # ---------------------------------------------------------
    teaching_domain = get_domain()
    dis.register_domain("teaching", teaching_domain)

    # ---------------------------------------------------------
    # 3. Register the real Teaching OSF Structure Pack
    teaching_structure = get_teaching_structure()
    osf.register_structure("teaching", "v1", teaching_structure)

    # ---------------------------------------------------------
    # 4. Load domain + structure
    # ---------------------------------------------------------
    domain_rules = dis.load_domain("teaching")
    structure = osf.load_structure("teaching", "v1")

    # ---------------------------------------------------------
    # 5. Run DIS
    # ---------------------------------------------------------
    instruction_set = dis.interpret(
        user_request="Help a learner talk about their weekend.",
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
    # 7. Run Rameon (with templates + flow logic)
    # ---------------------------------------------------------
    templates = get_teaching_templates()
    flow_logic = get_teaching_flow_logic()

    executed_output = rameon.execute(
        instruction_set=instruction_set,
        structure=structure,
        domain_rules=domain_rules,
        templates=templates,
        flow_logic=flow_logic
    )



    # ---------------------------------------------------------
    # 8. Run Governance validations
    # ---------------------------------------------------------
    domain_check = gov.validate_domain("teaching", instruction_set)
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
