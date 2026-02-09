from modules.constant import RuleId

from .base import Heuristic


class HeuristicName(Heuristic):
    def score(self, link):
        return 40 if link.rule_id == RuleId.NAME else 0
