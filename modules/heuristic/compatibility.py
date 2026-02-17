from modules.constant import RuleId

from .base import Heuristic


class HeuristicCompatibility(Heuristic):
    def score(self, link):
        if link.rule_id == RuleId.NAME and link.signature_mismatch():
            return -15
        return 0
