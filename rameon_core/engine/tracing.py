class TraceCollector:
    def __init__(self):
        self.steps = []

    def add(self, stage: str, data: dict):
        snapshot = {
            "stage": stage,
            "text": data.get("text", ""),
            "sections": data.get("sections", []),
        }
        self.steps.append(snapshot)

    def export(self):
        return self.steps
