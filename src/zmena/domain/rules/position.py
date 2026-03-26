from zmena.domain.model import Hypothesis
from zmena.domain.services.constant import RuleId

from .base import Rule


class RulePosition(Rule):
    def __init__(self):
        super().__init__(RuleId.POSITION)

    def apply(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_position_as(right):
                    hypothesis = Hypothesis(self.rule_id, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
