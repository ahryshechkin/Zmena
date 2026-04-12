from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel
from zmena.domain.types.rule_label import RuleLabel

from .base import Heuristic


class HeuristicSignature(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.SIGNATURE)

    def evaluate(self, hypothesis):
        if hypothesis.rule_label == RuleLabel.SIGNATURE:
            return [Evidence(hypothesis, 1.0, 0.9, self.label)]
        return []
