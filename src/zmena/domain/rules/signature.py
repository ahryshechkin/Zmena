from zmena.domain.model import Hypothesis
from zmena.domain.services.constant import RuleId

from .base import Rule


class RuleSignature(Rule):
    def __init__(self):
        super().__init__(RuleId.SIGNATURE)

    def apply(self, brick_bundle):
        bricks_left, bricks_right = brick_bundle.left(), brick_bundle.right()

        hypotheses = []
        for left in bricks_left:
            for right in bricks_right:
                if left is not right and left.same_signature_as(right):
                    hypothesis = Hypothesis(self.rule_id, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
