from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicCompatibility(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.COMPATIBILITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_name() and not hypothesis.has_same_signature():
            return [Evidence(hypothesis, -1.0, 0.4, self.label)]
        return []
