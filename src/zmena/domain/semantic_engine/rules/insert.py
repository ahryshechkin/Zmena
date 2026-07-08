from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments import StubFragment
from zmena.domain.semantic_engine.rules.rule import Rule
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side


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
