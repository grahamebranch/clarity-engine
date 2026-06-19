"""
RameonEngine - v1.0

Purpose:
- Orchestrate all engine layers in deterministic order
- Provide a single .process() entrypoint
- Ensure stable, predictable pipeline execution
"""

from engine_layer.osf import OSFShaping
from engine_layer.el3 import EL3Deterministic
from engine_layer.el4 import EL4Deterministic
from engine_layer.el5 import EL5Rewrite
from engine_layer.governance import GovernanceLayer
from engine_layer.final_output import FinalOutputLayer


class RameonEngine:
    def __init__(self):
        self.osf = OSFShaping()
        self.el3 = EL3Deterministic()
        self.el4 = EL4Deterministic()
        self.el5 = EL5Rewrite()
        self.gov = GovernanceLayer()
        self.final = FinalOutputLayer()

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def process(self, text: str) -> str:
        """
        Deterministic pipeline execution.
        """
        text = self.osf.osf(text)
        text = self.el3.el3(text)
        text = self.el4.el4(text)
        text = self.el5.el5(text)
        text = self.gov.governance(text)
        text = self.final.final_output(text)
        return text
