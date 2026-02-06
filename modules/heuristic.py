from abc import ABC, abstractmethod

from modules.constant import RuleId


class Heuristic(ABC):
    @abstractmethod
    def score(self, link):
        pass


class HeuristicName(Heuristic):
    def score(self, link):
        return 100 if link.rule_id == RuleId.NAME else 0


class HeuristicPosition(Heuristic):
    def score(self, link):
        return 50 if link.rule_id == RuleId.POSITION else 0


class HeuristicSignature(Heuristic):
    def score(self, link):
        return 25 if link.rule_id == RuleId.SIGNATURE else 0
