class Pipeline:
    """
    Real stage‑runner pipeline for the MVP Clarity Engine.
    Executes each stage in order, passing data through.
    """

    def __init__(self, stages=None):
        # Stages must be objects with a .run(data) method
        self.stages = stages or []

    def run(self, input_data):
        """
        Executes each stage in sequence.
        Whatever the last stage returns becomes the engine output.
        """
        data = input_data

        for stage in self.stages:
            # Each stage must implement .run(data)
            data = stage.run(data)

        return data
