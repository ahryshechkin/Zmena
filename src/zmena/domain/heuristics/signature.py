from zmena.domain.model.evidence import Evidence
from zmena.domain.types.rule_label import RuleLabel

from .base import Heuristic


class HeuristicSignature(Heuristic):
    def evaluate(self, hypothesis):
        if hypothesis.rule_id == RuleLabel.SIGNATURE:
            return [Evidence(self.__class__.__name__, hypothesis, 40)]
        return []
