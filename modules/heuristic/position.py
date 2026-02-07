from modules.constant import RuleId

from .base import Heuristic


class HeuristicPosition(Heuristic):
    def score(self, link):
        return 50 if link.rule_id == RuleId.POSITION else 0
