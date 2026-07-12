from zmena.domain.semantic_engine.core.hypothesis import Hypothesis
from zmena.domain.semantic_engine.fragments.stub import StubFragment
from zmena.domain.semantic_engine.rules.rule import Rule
from zmena.domain.semantic_engine.types.rule_kind import RuleKind
from zmena.domain.semantic_engine.types.side import Side


class HunkSurplusLeftRule(Rule):
    def __init__(self):
        super().__init__(RuleKind.HUNK_SURPLUS_LEFT)

    def generate(self, bundle):
        right_fragments_by_block = bundle.right_by_block()

        hypotheses = []
        for block, lefts in bundle.left_by_block().items():
            rights = right_fragments_by_block.get(block, [])

            if len(rights) >= len(lefts):
                continue

            if not all(fragment.is_replace() for fragment in lefts):
                continue

            if not all(fragment.is_replace() for fragment in rights):
                continue

            for fragment in lefts:
                stub_fragment = StubFragment(Side.RIGHT)
                hypothesis = Hypothesis(self.kind, fragment, stub_fragment)
                hypotheses.append(hypothesis)

        return hypotheses
