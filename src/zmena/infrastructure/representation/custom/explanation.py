class ReportExplanation:
    def __init__(self, explanation):
        self.explanation = explanation

    def render(self):
        for link in self.explanation.links:
            left, right = link.bricks

            evidences = []
            for evi in link.evidences:
                sign = "✔  +" if evi.score >= 0 else "✖  -"
                filler = " "
                evidence = f"{filler:<3}{sign}{abs(evi.score):<4}{evi.reason}\n"
                evidences.append(evidence)

            print(
                f"Link: {left.name} -> {right.name}\n"
                f"Score: {link.score}\n"
                f"Evidences:\n{''.join(evidences)}"
            )
