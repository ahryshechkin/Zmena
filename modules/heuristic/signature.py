from modules.constant import RuleId

from .base import Heuristic


class HeuristicSignature(Heuristic):
    def score(self, link):
        return 50 if link.rule_id == RuleId.SIGNATURE else 0
