from engine_layer.osf import OSFShaping
from engine_layer.el3 import EL3Deterministic
from engine_layer.el4 import EL4Deterministic
from engine_layer.el5 import EL5Rewrite
from engine_layer.el6 import EL6Deterministic
from engine_layer.el7 import EL7Deterministic
from engine_layer.el8 import EL8Deterministic
from engine_layer.el9 import EL9Deterministic
from engine_layer.el10 import EL10Deterministic
from engine_layer.governance import GovernanceLayer
from engine_layer.final_output import FinalOutputLayer


class RameonEngine:
    def __init__(self):
        self.osf = OSFShaping()
        self.el3 = EL3Deterministic()
        self.el4 = EL4Deterministic()
        self.el5 = EL5Rewrite()
        self.el6 = EL6Deterministic()
        self.el7 = EL7Deterministic()
        self.el8 = EL8Deterministic()
        self.el9 = EL9Deterministic()
        self.el10 = EL10Deterministic()
        self.gov = GovernanceLayer()
        self.final = FinalOutputLayer()

    def process(self, text: str) -> str:
        text = self.osf.osf(text)
        text = self.el3.el3(text)
        text = self.el4.el4(text)
        text = self.el5.el5(text)
        text = self.el6.el6(text)
        text = self.el7.el7(text)
        text = self.el8.el8(text)
        text = self.el9.el9(text)
        text = self.el10.el10(text)
        text = self.gov.governance(text)
        text = self.final.final_output(text)
        return text
