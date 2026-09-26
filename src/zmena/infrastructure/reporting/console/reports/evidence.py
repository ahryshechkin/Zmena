from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class EvidenceReport:
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
            print(self.formatted_line(link.header()))
            print(self.formatted_line(link.score()))

            evidences = link.evidence_bundle()
            if not evidences:
                print(self.formatted_line("Evidences: No data"))
            else:
                print(self.formatted_line("Evidences:"))
                for evidence in evidences:
                    print(self.formatted_line(self.styled_evidence(evidence)))

            self.separator()

    def formatted_line(self, line):
        visible_width = self.color.calculate_visible_width(line)
        padding = " " * max(0, self.decision.width(self.prefix) - visible_width)
        return f"| {line}{padding} |"

    def styled_evidence(self, evidence):
        filler = " " * 3
        polarity = evidence.polarity()
        mark = self.color.style_sign(polarity)
        return f"{filler}{mark}{polarity:>3}{evidence.description()}"

    def separator(self):
        sep = "-" * self.decision.width(self.prefix)
        print(f"+-{sep}-+")
