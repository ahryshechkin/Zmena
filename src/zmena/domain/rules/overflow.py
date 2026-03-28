from zmena.domain.model.brick.stub import BrickStub
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

        bricks_left_by_segment = {}
        for brick in bundle.left():
            bricks_left_by_segment.setdefault(brick.segment, []).append(brick)

        bricks_right_by_segment = {}
        for brick in bundle.right():
            bricks_right_by_segment.setdefault(brick.segment, []).append(brick)

        hypotheses = []
        for segment, rights in bricks_right_by_segment.items():
            lefts = bricks_left_by_segment.get(segment, [])

            if len(lefts) >= len(rights):
                continue

            if not all(brick.tag == Tag.REPLACE for brick in lefts):
                continue

            if not all(brick.tag == Tag.REPLACE for brick in rights):
                continue

            for brick in rights:
                brick_stub = BrickStub(Side.LEFT)
                hypothesis = Hypothesis(self.label, brick_stub, brick)
                hypotheses.append(hypothesis)

        return hypotheses
