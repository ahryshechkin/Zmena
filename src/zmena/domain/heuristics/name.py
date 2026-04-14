from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .base import Heuristic


class HeuristicName(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.NAME)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_name():
            return [Evidence(hypothesis, 1.0, 1.0, self.label)]
        return []
