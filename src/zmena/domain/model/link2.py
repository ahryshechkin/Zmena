class Link:
    def __init__(self, hypothesis):
        self.rule_id = hypothesis.rule_id
        self.left = hypothesis.left
        self.right = hypothesis.right
        self.evidence = []

    def bricks(self):
        return self.left, self.right

    def add_evidence(self, evidence):
        self.evidence.append(evidence)

    def conflicts_with(self, used_bricks):
        return self.left in used_bricks or self.right in used_bricks
