from zmena.domain.model.evidence import Evidence
from zmena.domain.services.constant import RuleId

from .base import Heuristic


class HeuristicName(Heuristic):
    def evaluate(self, hypothesis):
        if hypothesis.rule_id == RuleId.NAME:
            return [Evidence(self.__class__.__name__, hypothesis, 50)]
        return []
