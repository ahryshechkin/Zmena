import re

from zmena.infrastructure.reporting.console.ansi_color import ANSIColor


class StatementView:
    def __init__(self, kind, attrs):
        self.kind = kind
        self.attrs = attrs
        self.color = ANSIColor()

    def __str__(self):
        attrs = ",".join(f"{k}={v}" for k, v in self.attrs.items())
        return f"{self.kind}({attrs})"

    def __repr__(self):
        return f"StatementView(attrs={len(self.attrs)})"

    def render(self):
        pattern = re.compile(r"\b[A-Za-z_]\w*(?==)")
        return pattern.sub(self.highlight, str(self))

    def highlight(self, match):
        return f"{self.color.TERRACOTTA}{match.group()}{self.color.RESET}"

    def width(self):
        return len(str(self))
