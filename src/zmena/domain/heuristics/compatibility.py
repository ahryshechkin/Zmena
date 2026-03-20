from zmena.domain.services.constant import RuleId

from .base import Heuristic


class HeuristicCompatibility(Heuristic):
    def score(self, hypothesis):
        if hypothesis.rule_id == RuleId.NAME and hypothesis.signature_mismatch():
            return -15
        return 0
