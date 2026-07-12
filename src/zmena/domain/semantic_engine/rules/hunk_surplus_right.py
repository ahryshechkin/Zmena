from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.stub import StubFragment
from zmena.domain.semantic_engine.rules.rule import Rule
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side


class HunkSurplusRightRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.HUNK_SURPLUS_RIGHT)

    def generate(self, bundle):
        left_fragments_by_block = bundle.left_by_block()

        hypotheses = []
        for block, rights in bundle.right_by_block().items():
            lefts = left_fragments_by_block.get(block, [])

            if len(lefts) >= len(rights):
                continue

            if not all(fragment.is_replace() for fragment in lefts):
                continue

            if not all(fragment.is_replace() for fragment in rights):
                continue

            for fragment in rights:
                stub_fragment = StubFragment(Side.LEFT)
                hypothesis = Hypothesis(self.kind, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
