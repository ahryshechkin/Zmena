class LinkView:
    def __init__(self, total_score, left, right, evidences):
        self.total_score = total_score
        self.left = left
        self.right = right
        self.evidences = evidences

    def __str__(self):
        return f"{self.total_score:>7} | #### | {self.left} | #### | {self.right}"

    def header(self):
        left = self.left.caption()
        right = self.right.caption()
        return f"Link: {left} -> {right}"

    def score(self):
        return f"Score: {self.total_score}"

    def evidence_bundle(self):
        return self.evidences
