from modules.constant import RuleId, Side
from modules.model import Link, StubBrick

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleId.DELETE)


    def apply(self, scopes):
        bricks = scopes[0]
        links = list()
        for brick in bricks:
            if brick.is_delete():
                stub_brick = StubBrick(Side.RIGHT)
                link = Link(self.rule_id, brick, stub_brick)
                links.append(link)

        return links
