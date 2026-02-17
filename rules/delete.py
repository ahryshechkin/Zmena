from core.constant import RuleId, Side
from model import BrickStub, Link

from .base import Rule


class RuleDelete(Rule):
    def __init__(self):
        super().__init__(RuleId.DELETE)


    def apply(self, scopes):
        bricks = scopes[0]

        links = list()
        for brick in bricks:
            if brick.is_delete():
                brick_stub = BrickStub(Side.RIGHT)
                link = Link(self.rule_id, brick, brick_stub)
                links.append(link)

        return links
