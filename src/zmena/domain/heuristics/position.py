from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicPosition(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.POSITION)

    def evaluate(self, hypothesis):
        left, right = hypothesis.key()
        if left.same_position_as(right):
            return [Evidence(hypothesis, 1.0, 0.5, self.label)]
        return []
