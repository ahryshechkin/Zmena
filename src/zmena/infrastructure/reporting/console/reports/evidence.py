import re

from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class EvidenceReport:
    ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

    def __init__(self, name, decision):
        self.color = ANSIColor()
        self.prefix = f"#### {name} "
        self.decision = decision

    def __repr__(self):
        return "Report(specialized=Evidence)"

    def render(self):
        self.title()
        self.body()

    def title(self):
        width = self.decision.width(self.prefix) - len(self.prefix) + 4
        print(f"\n{self.prefix}" + "#" * width)

    def body(self):
        for link in self.decision.link_bundle():
            print(self.normalize(link.formatted_header()))
            print(self.normalize(link.formatted_score()))

            evidences = link.evidence_bundle()
            if not evidences:
                print(self.normalize("Evidences: No data"))
            else:
                print(self.normalize("Evidences:"))
                for evidence in evidences:
                    print(self.normalize(self.format(evidence)))

            self.separator()

    def normalize(self, line):
        padding = " " * (self.decision.width(self.prefix) - len(self.ANSI_RE.sub("", line)))
        return f"| {line}{padding} |"

    def format(self, evidence):
        filler = " " * 3
        polarity = evidence.polarity()
        mark = self.color.style_sign(polarity)
        return f"{filler}{mark}{polarity:>3}{evidence.description()}"

    def separator(self):
        sep = "-" * self.decision.width(self.prefix)
        print(f"+-{sep}-+")
