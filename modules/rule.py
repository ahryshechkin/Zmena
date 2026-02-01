from abc import ABC, abstractmethod
from brick import StubBrick
from constant import RuleId, Side, Tag
from link import Link


class Rule(ABC):
    def __init__(self, rule_id):
        self.rule_id = rule_id


    @abstractmethod
    def apply(self, scopes):
        pass


class RuleName(Rule):
    def __init__(self):
        super().__init__(RuleId.NAME)


    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        links = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_name(right):
                    link = Link(self.rule_id, left, right)
                    links.append(link)

        return links


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


class RuleSignature(Rule):
    def __init__(self):
        super().__init__(RuleId.SIGNATURE)


    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        links = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_signature(right):
                    link = Link(self.rule_id, left, right)
                    links.append(link)

        return links


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


class RuleInsert(Rule):
    def __init__(self):
        super().__init__(RuleId.INSERT)


    def apply(self, scopes):
        bricks = scopes[1]
        links = list()

        for brick in bricks:
            if brick.is_insert():
                stub_brick = StubBrick(Side.LEFT)
                link = Link(self.rule_id, stub_brick, brick)
                links.append(link)

        return links
