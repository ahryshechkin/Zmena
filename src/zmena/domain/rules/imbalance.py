from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.rules.rule import Rule
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side


class ImbalanceRule(Rule):
    def __init__(self):
        super().__init__(RuleLabel.IMBALANCE)

    def generate(self, bundle):
        left_fragments_by_segment = bundle.left_by_segment()

        hypotheses = []
        for segment, rights in bundle.right_by_segment().items():
            lefts = left_fragments_by_segment.get(segment, [])

            if len(lefts) >= len(rights):
                continue

            if not all(fragment.is_replace() for fragment in lefts):
                continue

            if not all(fragment.is_replace() for fragment in rights):
                continue

            for fragment in rights:
                stub_fragment = StubFragment(Side.LEFT)
                hypothesis = Hypothesis(self.label, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
