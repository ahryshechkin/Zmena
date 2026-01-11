from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def match(self, left, right):
        pass


class NameRule(Rule):
    def match(self, left, right):
        return left.name == right.name


class PositionRule(Rule):
    def match(self, left, right):
        return left.position == right.position