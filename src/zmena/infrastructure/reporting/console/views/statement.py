import re

from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class StatementView:
    def __init__(self, statement):
        self.color = ANSIColor()
        self.statement = statement

    def render(self):
        pattern = re.compile(r"\b[A-Za-z_]\w*(?==)")
        return pattern.sub(self.colorize, str(self.statement))

    def colorize(self, match):
        return f"{self.color.TERRACOTTA}{match.group()}{self.color.RESET}"

    def measure(self):
        return len(repr(self.statement))
