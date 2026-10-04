class LinkView:
    def __init__(self, score, left, right, evidences):
        self.score = score
        self.left = left
        self.right = right
        self.evidences = evidences

    def __str__(self):
        return f"{self.score:>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"LinkView(score={self.score},evidences={len(self.evidences)})"

    def header(self):
        left = self.left.caption()
        right = self.right.caption()
        return f"Link: {left} -> {right}"

    def formatted_score(self):
        return f"Score: {self.score}"

    def evidence_bundle(self):
        return self.evidences
