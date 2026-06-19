from rameon_engine import RameonEngine

if __name__ == "__main__":
    engine = RameonEngine()
    messy_input = "  this  is   a test...with  bad spacing!!and punctuation??and weird\n\n\nstructure. "
    output = engine.process(messy_input)
    print("=== OUTPUT START ===")
    print(repr(output))
    print("=== OUTPUT END ===")
