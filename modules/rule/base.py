from abc import ABC, abstractmethod


class Rule(ABC):
    def __init__(self, rule_id):
        self.rule_id = rule_id


    @abstractmethod
    def apply(self, scopes):
        pass
