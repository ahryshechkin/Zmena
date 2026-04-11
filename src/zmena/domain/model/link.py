from zmena.domain.explanations.link import ExplanationLink


class Link:
    def __init__(self, hypothesis):
        self.left = hypothesis.left
        self.right = hypothesis.right
        self.evidences = []

    def __str__(self):
        return f"{self.score():>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"Link(score={self.score()},evidences={len(self.evidences)})"

    def __lt__(self, other):
        return self.score() < other.score()

    def score(self):
        return sum(evidence.score for evidence in self.evidences)

    def bricks(self):
        return self.left, self.right

    def add_evidence(self, evidence):
        self.evidences.append(evidence)

    def conflicts_with(self, used_bricks):
        return self.left in used_bricks or self.right in used_bricks

    def justification(self):
        return ExplanationLink(
            bricks=self.bricks(),
            score=self.score(),
            evidences=list(self.evidences),
        )
