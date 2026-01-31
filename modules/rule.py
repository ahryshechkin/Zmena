from abc import ABC, abstractmethod
from link import Link


class Rule(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply(self, scopes):
        pass


class RuleName(Rule):
    def __init__(self):
        super().__init__("RuleName")


    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        links = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_name(right):
                    links.append(Link(self.name, left, right))

        return links


class RulePosition(Rule):
    def __init__(self):
        super().__init__("RulePosition")


    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        links = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_position(right):
                    links.append(Link(self.name, left, right))

        return links


class RuleDelete(Rule):
    def __init__(self):
        super().__init__("RuleDelete")


    def apply(self, scopes):
        bricks = scopes[0]
        links = list()
        for brick in bricks:
            if brick.is_delete():
                links.append(Link(self.name, brick, None))

        return links


class RuleInsert(Rule):
    def __init__(self):
        super().__init__("RuleInsert")


    def apply(self, scopes):
        bricks = scopes[1]
        links = list()

        for brick in bricks:
            if brick.is_insert():
                links.append(Link(self.name, brick, None))

        return links
