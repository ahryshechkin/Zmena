from .base import Link


class ScoredLink(Link):
    def __init__(self, score, link):
        super().__init__(link.rule_id, link.left, link.right)
        self.score = score


    def __str__(self):
        return f"{self.score:>7} | {super().__str__()}"


    def __repr__(self):
        return f"ScoredLink(score={self.score})"


    def __lt__(self, other):
        return self.score < other.score


    def bricks(self):
        return self.left, self.right


    def conflicts_with(self, used_bricks):
        return self.left in used_bricks or self.right in used_bricks
