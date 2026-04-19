from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleLabel.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for brick in bundle.left():
            if brick.is_delete():
                brick_stub = StubFragment(Side.RIGHT)
                hypothesis = Hypothesis(self.label, brick, brick_stub)
                hypotheses.append(hypothesis)

        return hypotheses
