from zmena.domain.model.evidence import Evidence
from zmena.domain.services.constant import RuleId

from .base import Heuristic


class HeuristicPosition(Heuristic):
    def evaluate(self, hypothesis):
        if hypothesis.rule_id == RuleId.POSITION:
            return [Evidence(self.__class__.__name__, hypothesis, 30)]
        return []
