from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicCompatibility(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.COMPATIBILITY)

    def evaluate(self, hypothesis):
        left, right = hypothesis.key()
        if left.same_name_as(right) and hypothesis.signature_mismatch():
            return [Evidence(hypothesis, -1.0, 0.4, self.label)]
        return []
