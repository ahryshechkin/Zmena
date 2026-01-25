from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def match(self, left, right):
        pass


class RuleName(Rule):
    def match(self, left, right):
        return left.compare_by_name(right)


class RulePosition(Rule):
    def match(self, left, right):
        return left.compare_by_position(right)


class RuleDelete(Rule):
    def match(self, left, right=None):
        pass