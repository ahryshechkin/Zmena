from zmena.domain.model.evidence import Evidence
from zmena.domain.types.rule_label import RuleLabel

from .base import Heuristic


class HeuristicName(Heuristic):
    def evaluate(self, hypothesis):
        if hypothesis.rule_label == RuleLabel.NAME:
            return [Evidence(self.__class__.__name__, hypothesis, 50)]
        return []
