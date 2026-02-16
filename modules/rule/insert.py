from modules.constant import RuleId, Side
from modules.model import BrickStub, Link

from .base import Rule


class RuleInsert(Rule):
    def __init__(self):
        super().__init__(RuleId.INSERT)


    def apply(self, scopes):
        bricks = scopes[1]

        links = list()
        for brick in bricks:
            if brick.is_insert():
                brick_stub = BrickStub(Side.LEFT)
                link = Link(self.rule_id, brick_stub, brick)
                links.append(link)

        return links
