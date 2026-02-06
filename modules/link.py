class Link:
    def __init__(self, rule_id, left, right):
        self.rule_id = rule_id
        self.left = left
        self.right = right


    def __str__(self):
        return (
            f"{self.rule_id.value:>9} | #### | {self.left} #### | {self.right}"
        )


    def __repr__(self):
        return (
            f"Link(rule_id={self.rule_id.value})"
        )


class ScoredLink(Link):
    def __init__(self, score, link):
        super().__init__(link.rule_id, link.left, link.right)
        self.score = score


    def __str__(self):
        return (
            f"{self.score:>7} | {super().__str__()}"
        )


    def __repr__(self):
        return f"ScoredLink(score={self.score})"


    def __lt__(self, other):
        return self.score < other.score
