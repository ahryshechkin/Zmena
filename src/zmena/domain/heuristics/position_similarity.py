from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicPositionSimilarity(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.POSITION_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_position():
            return [Evidence(hypothesis, 1.0, 0.3, self.label)]
        return []
