import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from rameon_core.engine.simple_engine import SimpleEngine
import json

test_text = """
we’re gonna fix it a bit later. It’s not ideal but we’ll sort it out.
I think we need to start the process and give people time to respond.
"""

def main():
    engine = SimpleEngine()
    engine.load({})

    # Tell the engine to use formal mode
    result = engine.run(test_text, user_request="formal")

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
