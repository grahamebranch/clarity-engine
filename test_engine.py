import sys, os
sys.path.append(os.path.dirname(__file__))

from rameon_core.engine.simple_engine import SimpleEngine

test_text = """Introduction
This is the intro text.

What is the purpose?
The purpose is to test the engine.

Steps
Step 1
Step 2
"""

def main():
    engine = SimpleEngine()
    engine.load({})

    result = engine.run(test_text)

    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
