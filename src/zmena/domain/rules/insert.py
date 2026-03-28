from zmena.domain.model.brick.stub import BrickStub
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side

from .base import Rule


class RuleInsert(Rule):
    def __init__(self):
        super().__init__(RuleLabel.INSERT)

    def generate(self, bundle):
        hypotheses = []
        for brick in bundle.right():
            if brick.is_insert():
                brick_stub = BrickStub(Side.LEFT)
                hypothesis = Hypothesis(self.rule_id, brick_stub, brick)
                hypotheses.append(hypothesis)

        return hypotheses
