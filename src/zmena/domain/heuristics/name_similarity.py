from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicNameSimilarity(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.NAME_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_name():
            return [Evidence(hypothesis, 1.0, 1.0, self.label)]
        return []
