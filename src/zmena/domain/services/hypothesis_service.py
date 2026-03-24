from zmena.domain.rules import (
    RuleDelete,
    RuleInsert,
    RuleName,
    RuleOverflow,
    RulePosition,
    RuleSignature,
)

from .matcher import Matcher


class HypothesisService:
    def __init__(self, brick_bundle):
        self.brick_bundle = brick_bundle

    def propose(self):
        matcher = Matcher(self.brick_bundle.left(), self.brick_bundle.right())

        hypotheses = []
        for rule in [
            RuleDelete(),
            RuleInsert(),
            RuleName(),
            RuleOverflow(),
            RulePosition(),
            RuleSignature(),
        ]:
            hypotheses.extend(matcher.match(rule))

        return hypotheses
