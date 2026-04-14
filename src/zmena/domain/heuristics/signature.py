from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicSignature(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.SIGNATURE)

    def evaluate(self, hypothesis):
        left, right = hypothesis.key()
        if left.same_signature_as(right):
            return [Evidence(hypothesis, 1.0, 0.9, self.label)]
        return []
