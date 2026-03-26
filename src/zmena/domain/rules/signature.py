from zmena.domain.model import Hypothesis
from zmena.domain.services.constant import RuleId

from .base import Rule


class RuleSignature(Rule):
    def __init__(self):
        super().__init__(RuleId.SIGNATURE)

    def generate(self, bundle):
        hypotheses = []
        for left in bundle.left():
            for right in bundle.right():
                if left is not right and left.same_signature_as(right):
                    hypothesis = Hypothesis(self.rule_id, left, right)
                    hypotheses.append(hypothesis)

        return hypotheses
