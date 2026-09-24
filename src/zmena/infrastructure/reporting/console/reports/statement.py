import re

from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class StatementReport:
    ATTRIBUTE_PATTERN = re.compile(r"\b[A-Za-z_]\w*(?==)")

    def __init__(self, name, statements):
        self.prefix = f"#### {name} "
        self.statements = statements
        self.color = ANSIColor()

    def __repr__(self):
        return "Report(specialized=Statement)"

    def render(self):
        self.title()
        self.body()
        # self.separator()

    def title(self):
        width = len(self.prefix) + 4
        print(f"\n{self.prefix}" + "#" * width)

    def body(self):
        for statement in self.statements:
            print(self.ATTRIBUTE_PATTERN.sub(self.format, str(statement)))

    def normalize(self, line):
        padding = " " * (
            self.decision_projection.width(self.prefix) - len(self.ANSI_RE.sub("", line))
        )
        return f"| {line}{padding} |"

    def format(self, match):
        return f"{self.color.TERRACOTTA}{match.group()}{self.color.RESET}"

    def separator(self):
        sep = "-" * self.decision_projection.width(self.prefix)
        print(f"+-{sep}-+")
