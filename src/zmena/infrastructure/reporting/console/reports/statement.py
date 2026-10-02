from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class StatementReport:
    def __init__(self, name, statements):
        self.prefix = f"#### {name} "
        self.statements = statements
        self.color = ANSIColor()

    def __repr__(self):
        return "Report(specialized=Statement)"

    def render(self):
        self.title()
        self.body()
        self.separator()

    def title(self):
        width = self.width() - len(self.prefix) + 4
        print(f"\n{self.prefix}" + "#" * width)

    def body(self):
        for statement in self.statements:
            print(self.formatted_line(statement.render()))

    def formatted_line(self, line):
        visible_width = self.color.calculate_visible_width(line)
        padding = " " * max(0, self.width() - visible_width)
        return f"| {line}{padding} |"

    def separator(self):
        sep = "-" * self.width()
        print(f"+-{sep}-+")

    def width(self):
        return max(statement.width() for statement in self.statements)
