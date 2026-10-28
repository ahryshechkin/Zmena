from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class ScriptReport:
    def __init__(self, name, scripts):
        self.prefix = f"#### {name} "
        self.scripts = scripts
        self.color = ANSIColor()

    def __repr__(self):
        return "Report(specialized=Script)"

    def render(self):
        self.title()
        self.body()
        self.separator()

    def title(self):
        width = self.width() - len(self.prefix) + 4
        print(f"\n{self.prefix}" + "#" * width)

    def body(self):
        if not self.scripts:
            print(self.formatted_line("No data to show"))
        else:
            for script in self.scripts:
                print(self.formatted_line(script.render()))

    def formatted_line(self, line):
        padding = " " * max(0, self.width())
        return f"| {line}{padding} |"

    def separator(self):
        sep = "-" * self.width()
        print(f"+-{sep}-+")

    def width(self):
        return max((script.width() for script in self.scripts), default=15)
