from domain.services import RuleId, Side, Tag
from domain.model import BrickStub, Link

from .base import Rule


class RuleOverflow(Rule):
    def __init__(self):
        super().__init__(RuleId.OVERFLOW)


    def apply(self, scopes):
        bricks_left, bricks_right = scopes[:2]

        bricks_left_by_segment = dict()
        for brick in bricks_left:
            bricks_left_by_segment.setdefault(brick.segment, []).append(brick)

        bricks_right_by_segment = dict()
        for brick in bricks_right:
            bricks_right_by_segment.setdefault(brick.segment, []).append(brick)

        links = list()
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
                link = Link(self.rule_id, brick_stub, brick)
                links.append(link)

        return links
