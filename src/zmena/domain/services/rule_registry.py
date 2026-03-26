from zmena.domain.rules import (
    RuleDelete,
    RuleInsert,
    RuleName,
    RuleOverflow,
    RulePosition,
    RuleSignature,
)


class RuleRegistry:
    def __init__(self):
        self.delete = RuleDelete()
        self.insert = RuleInsert()
        self.name = RuleName()
        self.overflow = RuleOverflow()
        self.position = RulePosition()
        self.signature = RuleSignature()

    def default_rules(self):
        return [
            self.delete,
            self.insert,
            self.name,
            self.overflow,
            self.position,
            self.signature,
        ]
