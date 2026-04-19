from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side

from .base import Rule


class RuleInsert(Rule):
    def __init__(self):
        super().__init__(RuleLabel.INSERT)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.right():
            if fragment.is_insert():
                stub_fragment = StubFragment(Side.LEFT)
                hypothesis = Hypothesis(self.label, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
