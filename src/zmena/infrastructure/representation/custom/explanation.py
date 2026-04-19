import re

from zmena.infrastructure.representation.color import Color


class ExplanationReport:
    ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

    def __init__(self, name, decision_explanation):
        self.name = name
        self.decision_explanation = decision_explanation
        self.color = Color()

    def render(self):
        self.title()
        self.body()

    def title(self):
        prefix = f"#### {self.name} "
        width = self.decision_explanation.width() - len(prefix) + 4
        print(f"\n{prefix}" + "#" * width)

    def body(self):
        for link_explanation in self.decision_explanation.explain():
            print(self.normalize(link_explanation.formatted_header()))
            print(self.normalize(link_explanation.formatted_score()))

            print(self.normalize("Evidences:"))
            for evidence in link_explanation.evidences():
                print(self.normalize(self.format(evidence)))

            self.separator()

    def normalize(self, line):
        padding = " " * (self.decision_explanation.width() - len(self.ANSI_RE.sub("", line)))
        return f"| {line}{padding} |"

    def format(self, evidence):
        filler = " " * 3
        sign = evidence.sign()
        mark = self.color.style_sign(sign)
        return f"{filler}{mark}{sign:>3}{evidence.describe()}"

    def separator(self):
        sep = "-" * self.decision_explanation.width()
        print(f"+-{sep}-+")
