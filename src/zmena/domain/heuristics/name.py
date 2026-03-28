from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel
from zmena.domain.types.rule_label import RuleLabel

from .base import Heuristic


class HeuristicName(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.NAME)

    def evaluate(self, hypothesis):
        if hypothesis.rule_label == RuleLabel.NAME:
            return [Evidence(self.label, hypothesis, 50)]
        return []
