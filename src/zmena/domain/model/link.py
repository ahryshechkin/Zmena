class Link:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.evidences = []

    def __str__(self):
        return f"{self.score():>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"Link(score={self.score()},evidences={len(self.evidences)})"

    def __lt__(self, other):
        return self.score() < other.score()

    def fragments(self):
        return self.left, self.right

    def justification(self):
        return self.evidences

    def score(self):
        return round(sum(evidence.score() for evidence in self.evidences), 1)

    def add_evidence(self, evidence):
        self.evidences.append(evidence)

    def conflicts_with(self, used_fragments):
        return self.left in used_fragments or self.right in used_fragments
