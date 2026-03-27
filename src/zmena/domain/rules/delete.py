from zmena.domain.model import BrickStub, Hypothesis
from zmena.domain.services.constant import Side
from zmena.domain.types.rule_label import RuleLabel

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleLabel.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for brick in bundle.left():
            if brick.is_delete():
                brick_stub = BrickStub(Side.RIGHT)
                hypothesis = Hypothesis(self.rule_id, brick, brick_stub)
                hypotheses.append(hypothesis)

        return hypotheses
