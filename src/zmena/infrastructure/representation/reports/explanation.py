import re

from zmena.infrastructure.representation.ansi_color import ANSIColor


class ExplanationReport:
    ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

    def __init__(self, name, decision_projection):
        self.name = name
        self.decision_projection = decision_projection
        self.color = ANSIColor()

    def __repr__(self):
        return "Report(specialized=Explanation)"

    def render(self):
        self.title()
        self.body()

    def title(self):
        prefix = f"#### {self.name} "
        width = self.decision_projection.width() - len(prefix) + 4
        print(f"\n{prefix}" + "#" * width)

    def body(self):
        for link_projection in self.decision_projection.links():
            print(self.normalize(link_projection.formatted_header()))
            print(self.normalize(link_projection.formatted_score()))

            evidences = link_projection.evidences()
            if not evidences:
                print(self.normalize("Evidences: No data"))
            else:
                print(self.normalize("Evidences:"))
                for evidence in evidences:
                    print(self.normalize(self.format(evidence)))

            self.separator()

    def normalize(self, line):
        padding = " " * (self.decision_projection.width() - len(self.ANSI_RE.sub("", line)))
        return f"| {line}{padding} |"

    def format(self, evidence):
        filler = " " * 3
        polarity = evidence.polarity()
        mark = self.color.style_sign(polarity)
        return f"{filler}{mark}{polarity:>3}{evidence.description()}"

    def separator(self):
        sep = "-" * self.decision_projection.width()
        print(f"+-{sep}-+")
