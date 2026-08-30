from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.kinds.rule import RuleKind
from zmena.domain.semantic_engine.rules.rule import Rule


class PositionRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.POSITION)

    def generate(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_position_as(right):
                    hypothesis = Hypothesis(self.kind, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
