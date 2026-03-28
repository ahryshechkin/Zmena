class Link:
    def __init__(self, hypothesis):
        self.rule_label = hypothesis.rule_label
        self.left = hypothesis.left
        self.right = hypothesis.right
        self.evidences = []

    def __str__(self):
        score = sum(evidence.score for evidence in self.evidences)
        return f"{score:>7} | {self.rule_label.value:>9} | #### | {self.left} #### | {self.right}"

    def __repr__(self):
        score = sum(evidence.score for evidence in self.evidences)
        return f"Link(score={score})"

    def __lt__(self, other):
        score_self = sum(evidence.score for evidence in self.evidences)
        score_other = sum(evidence.score for evidence in other.evidences)
        return score_self < score_other

    def bricks(self):
        return self.left, self.right

    def add_evidence(self, evidence):
        self.evidences.append(evidence)

    def conflicts_with(self, used_bricks):
        return self.left in used_bricks or self.right in used_bricks
