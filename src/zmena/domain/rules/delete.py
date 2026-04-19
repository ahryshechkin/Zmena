from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side

from .rule import Rule


class DeleteRule(Rule):
    def __init__(self):
        super().__init__(RuleLabel.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.left():
            if fragment.is_delete():
                stub_fragment = StubFragment(Side.RIGHT)
                hypothesis = Hypothesis(self.label, fragment, stub_fragment)
                hypotheses.append(hypothesis)

        return hypotheses
