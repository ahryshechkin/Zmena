class ReportExplanation:
    def __init__(self, explanations):
        self.explanations = explanations

    def render(self):
        for explanation in self.explanations:
            left, right = explanation["bricks"]
            evidences = "\n".join([evidence["reason"] for evidence in explanation["evidences"]])
            print(f"Chosen link: {left.name} {right.name}\nbecause of:\n  {evidences}")
