from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.rules.rule import Rule
from zmena.domain.semantic_engine.types.rule_kind import RuleKind


class NameRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.NAME)

    def generate(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_name_as(right):
                    hypothesis = Hypothesis(self.kind, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
