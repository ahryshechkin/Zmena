from zmena.domain.rules.delete import DeleteRule
from zmena.domain.rules.insert import InsertRule
from zmena.domain.rules.name import NameRule
from zmena.domain.rules.overflow import OverflowRule
from zmena.domain.rules.position import PositionRule
from zmena.domain.rules.signature import SignatureRule


class RuleRegistry:
    def __init__(self):
        self.delete = DeleteRule()
        self.insert = InsertRule()
        self.name = NameRule()
        self.overflow = OverflowRule()
        self.position = PositionRule()
        self.signature = SignatureRule()

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
