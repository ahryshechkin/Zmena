from zmena.domain.explanations.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel
from zmena.domain.types.rule_label import RuleLabel

from .base import Heuristic


class HeuristicCompatibility(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.COMPATIBILITY)

    def evaluate(self, hypothesis):
        if hypothesis.rule_label == RuleLabel.NAME and hypothesis.signature_mismatch():
            return [Evidence(hypothesis, -1.0, 0.7, self.label)]
        return []
