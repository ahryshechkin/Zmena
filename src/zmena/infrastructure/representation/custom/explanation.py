import re

from zmena.infrastructure.representation.color import Color


class ReportExplanation:
    ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

    def __init__(self, explanation, name):
        self.name = name
        self.explanation = explanation
        self.color = Color()

    def render(self):
        self.title()
        self.body()

    def title(self):
        prefix = f"#### {self.name} "
        width = self.length() - len(prefix) + 4
        print(f"\n{prefix}" + "#" * width)

    def body(self):
        for link in self.explanation.links:
            print(self.normalize(self.reference_line(*link.bricks)))
            print(self.normalize(f"Score: {link.score}"))
            print(self.normalize("Evidences:"))

            for evidence in link.evidences:
                print(self.normalize(self.format(evidence)))

            self.separator()

    def length(self):
        return max(len(self.reference_line(*link.bricks)) for link in self.explanation.links)

    def reference_line(self, left, right):
        return (
            f"Link: "
            f"{left.name} ({left.side}:{left.position})"
            f" -> "
            f"{right.name} ({right.side}:{right.position})"
        )

    def normalize(self, line):
        padding = " " * (self.length() - len(self.ANSI_RE.sub("", line)))
        return f"| {line}{padding} |"

    def format(self, evidence):
        filler = " " * 3
        sign = "+" if evidence.score >= 0 else "-"
        mark = self.color.style_sign(sign)
        return f"{filler}{mark}{sign:>3}{abs(evidence.score):<4}{evidence.reason}"

    def separator(self):
        sep = "-" * self.length()
        print(f"+-{sep}-+")
