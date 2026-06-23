# rameon_engine.py
# Thin wrapper around engine_layer.RameonEngine

from engine_layer.rameon import RameonEngine as LayerRameonEngine


class RameonEngine:
    def __init__(self):
        self.engine = LayerRameonEngine()

    def run(self, text: str) -> str:
        result = self.engine.process(text)

        # FastPath: unwrap ("text",) → "text"
        if isinstance(result, tuple) and len(result) == 1:
            return result[0]

        return result
