from zmena.domain.model.fragments.stub import StubFragment
from zmena.domain.model.hypothesis import Hypothesis
from zmena.domain.types.rule_label import RuleLabel
from zmena.domain.types.side import Side
from zmena.domain.types.tag import Tag

from .base import Rule


class RuleOverflow(Rule):
    def __init__(self):
        super().__init__(RuleLabel.OVERFLOW)

    def generate(self, bundle):
        bundle.right()

        fragments_left_by_segment = {}
        for fragment in bundle.left():
            fragments_left_by_segment.setdefault(fragment.segment, []).append(fragment)

        fragments_right_by_segment = {}
        for fragment in bundle.right():
            fragments_right_by_segment.setdefault(fragment.segment, []).append(fragment)

        hypotheses = []
        for segment, rights in fragments_right_by_segment.items():
            lefts = fragments_left_by_segment.get(segment, [])

            if len(lefts) >= len(rights):
                continue

            if not all(fragment.tag == Tag.REPLACE for fragment in lefts):
                continue

            if not all(fragment.tag == Tag.REPLACE for fragment in rights):
                continue

            for fragment in rights:
                stub_fragment = StubFragment(Side.LEFT)
                hypothesis = Hypothesis(self.label, stub_fragment, fragment)
                hypotheses.append(hypothesis)

        return hypotheses
