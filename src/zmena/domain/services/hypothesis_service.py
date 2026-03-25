from zmena.domain.rules import (
    RuleDelete,
    RuleInsert,
    RuleName,
    RuleOverflow,
    RulePosition,
    RuleSignature,
)


class HypothesisService:
    def __init__(self, brick_bundle):
        self.brick_bundle = brick_bundle

    def propose(self):
        hypotheses = []
        for rule in [
            RuleDelete(),
            RuleInsert(),
            RuleName(),
            RuleOverflow(),
            RulePosition(),
            RuleSignature(),
        ]:
            hypotheses.extend(rule.apply(self.brick_bundle))

        return hypotheses
