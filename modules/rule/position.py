from modules.constant import RuleId
from modules.model import Link

from .base import Rule


class RulePosition(Rule):
    def __init__(self):
        super().__init__(RuleId.POSITION)


    def apply(self, scopes):
        bricks_left, bricks_right = scopes[:2]

        links = list()
        for left in bricks_left:
            for right in bricks_right:
                if left is not right and left.same_position_as(right):
                    link = Link(self.rule_id, left, right)
                    links.append(link)

        return links
