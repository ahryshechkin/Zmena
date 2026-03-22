from zmena.domain.model.evidence import Evidence
from zmena.domain.services.constant import RuleId

from .base import Heuristic


class HeuristicSignature(Heuristic):
    def evaluate(self, hypothesis):
        if hypothesis.rule_id == RuleId.SIGNATURE:
            return [Evidence(self.__class__.__name__, hypothesis, 40)]
        return []
