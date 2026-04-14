from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicPosition(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.POSITION)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_position():
            return [Evidence(hypothesis, 1.0, 0.5, self.label)]
        return []
