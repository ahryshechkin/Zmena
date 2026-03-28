from zmena.domain.rules.delete import RuleDelete
from zmena.domain.rules.insert import RuleInsert
from zmena.domain.rules.name import RuleName
from zmena.domain.rules.overflow import RuleOverflow
from zmena.domain.rules.position import RulePosition
from zmena.domain.rules.signature import RuleSignature


class RuleRegistry:
    def __init__(self):
        self.delete = RuleDelete()
        self.insert = RuleInsert()
        self.name = RuleName()
        self.overflow = RuleOverflow()
        self.position = RulePosition()
        self.signature = RuleSignature()

    def __repr__(self):
        return "Registry(type=rule)"

    def default_rules(self):
        return [
            self.delete,
            self.insert,
            self.name,
            self.overflow,
            self.position,
            self.signature,
        ]
