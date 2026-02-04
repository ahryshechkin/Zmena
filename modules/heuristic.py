from abc import ABC, abstractmethod

from modules.constant import RuleId


class Heuristic(ABC):
    @abstractmethod
    def score(self, link):
        pass


class HeuristicName(Heuristic):
    def score(self, link):
        if link.rule_id == RuleId.NAME:
            return 100
        else:
            return 0


class HeuristicPosition(Heuristic):
    def score(self, link):
        if link.rule_id == RuleId.POSITION:
            return 50
        else:
            return 0
