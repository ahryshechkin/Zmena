from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.stub import StubFragment
from zmena.domain.semantic_engine.rules.rule import Rule
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side


class DeleteRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.DELETE)

    def generate(self, bundle):
        hypotheses = []
        for fragment in bundle.left():
            if fragment.is_delete():
                stub_fragment = StubFragment(Side.RIGHT)
                hypothesis = Hypothesis(self.kind, fragment, stub_fragment)
                hypotheses.append(hypothesis)

        return hypotheses
