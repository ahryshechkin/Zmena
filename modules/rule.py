from abc import ABC, abstractmethod
from brick import RightBrick


class Rule(ABC):
    @abstractmethod
    def apply(self, scopes):
        pass


class RuleName(Rule):
    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        pairs = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_name(right):
                    pairs.append((left, right))

        return pairs


class RulePosition(Rule):
    def apply(self, scopes):
        left_bricks, right_bricks = scopes[:2]
        pairs = list()
        for left in left_bricks:
            for right in right_bricks:
                if left is not right and left.compare_by_position(right):
                    pairs.append((left, right))

        return pairs


class RuleDelete(Rule):
    def apply(self, scopes):
        bricks = scopes[0]
        pairs = list()
        for brick in bricks:
            if brick.is_delete():
                pairs.append((brick, None))

        return pairs
