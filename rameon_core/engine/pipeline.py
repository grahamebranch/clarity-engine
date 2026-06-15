class Pipeline:
    """
    Real stage‑runner pipeline for the MVP Clarity Engine.
    Executes each stage in order, passing data through.
    """

    def __init__(self, stages=None):
        self.stages = stages or []

    def run(self, input_data):
        data = input_data

        for stage in self.stages:
            data = stage.run(data)

            # Integrate DIS5 metadata for Edition Logic
            if data.get("stage") == "DIS5":
                sections = data.get("sections", [])
                for sec in sections:
                    meta = sec.get("metadata", {})
                    sec["length"] = meta.get("length")
                    sec["avg_sentence_length"] = meta.get("avg_sentence_length")
                    sec["keywords"] = meta.get("keywords")
                    sec["density"] = meta.get("density")
                    sec["cohesion_score"] = meta.get("cohesion_score")

        return data
