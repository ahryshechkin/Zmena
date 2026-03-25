from zmena.domain.model import BrickStub, Hypothesis
from zmena.domain.services.constant import RuleId, Side

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleId.DELETE)

    def apply(self, brick_bundle):
        bricks = brick_bundle.left()

        hypotheses = []
        for brick in bricks:
            if brick.is_delete():
                brick_stub = BrickStub(Side.RIGHT)
                hypothesis = Hypothesis(self.rule_id, brick, brick_stub)
                hypotheses.append(hypothesis)

        return hypotheses
