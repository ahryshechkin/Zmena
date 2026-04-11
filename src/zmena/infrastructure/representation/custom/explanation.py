from zmena.infrastructure.representation.color import Color


class ReportExplanation:
    def __init__(self, explanation):
        self.explanation = explanation
        self.color = Color()

    def render(self):
        print()
        for link in self.explanation.links:
            left, right = link.bricks

            evidences = []
            for evidence in link.evidences:
                evi = self.format(evidence)
                evidences.append(evi)

            print(
                f"Link: "
                f"{left.name} ({left.side}:{left.position})"
                f" -> "
                f"{right.name} ({right.side}:{right.position})\n"
                f"Score: {link.score}\n"
                f"Evidences:\n{''.join(evidences)}"
            )

    def format(self, evidence):
        filler = " "

        sign = "+" if evidence.score >= 0 else "-"
        mark = self.color.style_sign(sign)

        return f"{filler:<3}{mark}{sign:>3}{abs(evidence.score):<4}{evidence.reason}\n"
