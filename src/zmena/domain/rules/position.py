from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel

from .base import Rule


class PositionRule(Rule):
    def __init__(self):
        super().__init__(RuleLabel.POSITION)

    def generate(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_position_as(right):
                    hypothesis = Hypothesis(self.label, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
