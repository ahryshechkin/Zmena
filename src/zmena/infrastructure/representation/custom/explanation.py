from zmena.infrastructure.representation.color import Color


class ReportExplanation:
    def __init__(self, explanation):
        self.explanation = explanation
        self.color = Color()

    def render(self):
        for link in self.explanation.links:
            left, right = link.bricks

            evidences = []
            for evi in link.evidences:
                filler = " "
                if evi.score >= 0:
                    sign = "+"
                    mark = self.color.colorize_sign(sign, "✔")
                else:
                    sign = "-"
                    mark = self.color.colorize_sign(sign, "✖")
                evidence = f"{filler:<3}{mark}{sign:>3}{abs(evi.score):<4}{evi.reason}\n"
                evidences.append(evidence)

            print(
                f"Link: {left.name} -> {right.name}\n"
                f"Score: {link.score}\n"
                f"Evidences:\n{''.join(evidences)}"
            )
