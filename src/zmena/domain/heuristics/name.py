from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicName(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.NAME)

    def evaluate(self, hypothesis):
        left, right = hypothesis.key()
        if left.same_name_as(right):
            return [Evidence(hypothesis, 1.0, 1.0, self.label)]
        return []
