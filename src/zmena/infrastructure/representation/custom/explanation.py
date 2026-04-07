class ReportExplanation:
    def __init__(self, explanation):
        self.explanation = explanation

    def render(self):
        for link in self.explanation.links:
            left, right = link.bricks
            score = link.score
            evidences = "\n".join(
                [f"{evidence.reason}    {evidence.score}" for evidence in link.evidences]
            )

            print(
                f"Chosen Link: {left.name} -> {right.name}\nScore: {score}\nEvidences:\n{evidences}"
            )
