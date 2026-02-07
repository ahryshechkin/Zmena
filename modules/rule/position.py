from modules.constant import RuleId
from modules.model import Link

from .base import Rule


class RulePosition(Rule):
    def __init__(self):
        super().__init__(RuleId.POSITION)


    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        links = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_position(right):
                    link = Link(self.rule_id, left, right)
                    links.append(link)

        return links
