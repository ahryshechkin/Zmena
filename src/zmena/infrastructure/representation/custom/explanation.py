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
        width = self.explanation.length() - len(prefix) + 4
        print(f"\n{prefix}" + "#" * width)

    def body(self):
        for explanation_link in self.explanation.links:
            print(self.normalize(explanation_link.summary()))
            print(self.normalize(f"Score: {explanation_link.score()}"))
            print(self.normalize("Evidences:"))

            for evidence in explanation_link.justification():
                print(self.normalize(self.format(evidence)))

            self.separator()

    def normalize(self, line):
        padding = " " * (self.explanation.length() - len(self.ANSI_RE.sub("", line)))
        return f"| {line}{padding} |"

    def format(self, evidence):
        filler = " " * 3
        sign = evidence.sign()
        mark = self.color.style_sign(sign)
        return f"{filler}{mark}{sign:>3}{evidence.describe()}"

    def separator(self):
        sep = "-" * self.explanation.length()
        print(f"+-{sep}-+")
