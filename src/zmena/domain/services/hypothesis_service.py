from zmena.domain.rules import (
    RuleDelete,
    RuleInsert,
    RuleName,
    RuleOverflow,
    RulePosition,
    RuleSignature,
)


class HypothesisService:
    def __init__(self, bundle):
        self.bundle = bundle

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
            hypotheses.extend(rule.generate(self.bundle))

        return hypotheses
