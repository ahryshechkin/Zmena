from zmena.domain.model import Hypothesis
from zmena.domain.types.rule_label import RuleLabel

from .base import Rule


class RuleName(Rule):
    def __init__(self):
        super().__init__(RuleLabel.NAME)

    def generate(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_name_as(right):
                    hypothesis = Hypothesis(self.rule_id, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
