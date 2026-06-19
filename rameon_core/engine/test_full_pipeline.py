"""
Full Pipeline Test — matches the new SimpleEngine output format.
"""

from .simple_engine import SimpleEngine


def run_full_pipeline_test():
    engine = SimpleEngine()

    test_input = """
    ## Test Heading

    This is a paragraph. It should be split into sections. The engine should detect structure.

    - item one
    - item two
    """

    print("\n==============================")
    print(" RUNNING FULL PIPELINE TEST")
    print("==============================\n")

    output = engine.run(test_input)

    print("=== TOPIC ===")
    print(output.get("topic"))
    print("\n")

    print("=== LEVEL ===")
    print(output.get("level"))
    print("\n")

    print("=== DOMAIN ===")
    print(output.get("domain"))
    print("\n")

    print("=== SECTIONS ===")
    lesson = output.get("lesson", {})
    for i, sec in enumerate(lesson.get("sections", []), 1):
        print(f"[{i}] {sec['title']}")
    print("\n")

    print("=== CLARITY ===")
    print(output.get("clarity"))
    print("\n")

    print("=== SUMMARY ===")
    print(output.get("summary"))
    print("\n")


if __name__ == "__main__":
    run_full_pipeline_test()
