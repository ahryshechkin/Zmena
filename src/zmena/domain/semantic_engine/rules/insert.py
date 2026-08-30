from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.stub import StubFragment
from zmena.domain.semantic_engine.kinds.rule import RuleKind
from zmena.domain.semantic_engine.kinds.side import SideKind
from zmena.domain.semantic_engine.rules.rule import Rule


class InsertRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.INSERT)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.right():
            if fragment.is_insert():
                stub_fragment = StubFragment(SideKind.LEFT)
                hypothesis = Hypothesis(self.kind, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
