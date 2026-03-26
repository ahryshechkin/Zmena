from zmena.domain.model import BrickStub, Hypothesis
from zmena.domain.services.constant import RuleId, Side

from .base import Rule


class RuleInsert(Rule):
    def __init__(self):
        super().__init__(RuleId.INSERT)

    def apply(self, bundle):
        hypotheses = []
        for brick in bundle.right():
            if brick.is_insert():
                brick_stub = BrickStub(Side.LEFT)
                hypothesis = Hypothesis(self.rule_id, brick_stub, brick)
                hypotheses.append(hypothesis)

        return hypotheses
