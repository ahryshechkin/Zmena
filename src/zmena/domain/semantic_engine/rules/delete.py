from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.stub import StubFragment
from zmena.domain.semantic_engine.kinds.rule import RuleKind
from zmena.domain.semantic_engine.kinds.side import SideKind
from zmena.domain.semantic_engine.rules.rule import Rule


class DeleteRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.left():
            if fragment.is_delete():
                stub_fragment = StubFragment(SideKind.RIGHT)
                hypothesis = Hypothesis(self.kind, fragment, stub_fragment)
                hypotheses.append(hypothesis)

        return hypotheses
