from zmena.domain.model import BrickStub, Hypothesis
from zmena.domain.services.constant import RuleId, Side

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleId.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for brick in bundle.left():
            if brick.is_delete():
                brick_stub = BrickStub(Side.RIGHT)
                hypothesis = Hypothesis(self.rule_id, brick, brick_stub)
                hypotheses.append(hypothesis)

        return hypotheses
