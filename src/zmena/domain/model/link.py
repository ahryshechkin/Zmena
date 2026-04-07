from zmena.domain.explanations.link import ExplanationLink


class Link:
    def __init__(self, hypothesis):
        self.left = hypothesis.left
        self.right = hypothesis.right
        self.evidences = []

    def __str__(self):
        score = sum(evidence.score for evidence in self.evidences)
        return f"{score:>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        score = sum(evidence.score for evidence in self.evidences)
        return f"Link(score={score},evidences={len(self.evidences)})"

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

    def justification(self):
        return ExplanationLink(
            bricks=self.bricks(),
            score=sum(evidence.score for evidence in self.evidences),
            evidences=list(self.evidences),
        )
