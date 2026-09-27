import re

from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class StatementView:
    def __init__(self, statement):
        self.statement = statement
        self.color = ANSIColor()

    def render(self):
        pattern = re.compile(r"\b[A-Za-z_]\w*(?==)")
        return pattern.sub(self.highlight, str(self.statement))

    def highlight(self, match):
        return f"{self.color.TERRACOTTA}{match.group()}{self.color.RESET}"

    def width(self):
        return len(repr(self.statement))
