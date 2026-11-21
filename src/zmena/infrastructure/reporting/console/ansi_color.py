import re

from zmena.domain.semantic_engine.kinds.opcode import OpcodeKind


class ANSIColor:
    GRAY = "\033[38;5;250m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    TERRACOTTA = "\033[38;2;170;73;38m"
    BOLD = "\033[1m"

    def __repr__(self):
        return "ANSIColor"

    def style_text(self, opcode, text):
        colors = {
            OpcodeKind.DELETE: self.RED,
            OpcodeKind.EQUAL: self.GRAY,
            OpcodeKind.INSERT: self.GREEN,
            OpcodeKind.REPLACE: self.YELLOW,
        }

        return f"{colors[opcode]}{text}{self.RESET}"

    def style_sign(self, sign):
        colors = {
            "-": ("x", self.RED),
            "+": ("v", self.GREEN),
        }

        mark, color = colors[sign]

        return f"{color}{self.BOLD}{mark}{self.RESET}"

    def calculate_visible_width(self, line):
        pattern = re.compile(r"\x1b\[[0-9;]*m")
        return len(pattern.sub("", line))
