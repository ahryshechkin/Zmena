from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.rules.rule import Rule
from zmena.domain.types.rule_kind import RuleKind
from zmena.domain.types.side import Side


class InsertRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.INSERT)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.right():
            if fragment.is_insert():
                stub_fragment = StubFragment(Side.LEFT)
                hypothesis = Hypothesis(self.kind, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
