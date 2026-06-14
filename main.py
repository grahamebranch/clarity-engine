from rameon_core.engine.simple_engine import SimpleEngine
from rameon_core.engine.context import EngineContext


def run_clarity_engine(user_input):
    context = EngineContext()
    engine = SimpleEngine()

    result = engine.run(user_input)

    print("\n=== OUTPUT ===")
    print(result)


if __name__ == "__main__":
    import sys
    print("Paste your text below. Press Ctrl+D when finished:\n")

    input_data = sys.stdin.read()

    run_clarity_engine(input_data)
