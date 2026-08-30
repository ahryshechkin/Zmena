from zmena.domain.semantic_engine.kinds.tag import TagKind


class ANSIColor:
    GRAY = "\033[38;5;250m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def __repr__(self):
        return "ANSIColor"

    def style_text(self, tag, text):
        colors = {
            TagKind.DELETE: self.RED,
            TagKind.EQUAL: self.GRAY,
            TagKind.INSERT: self.GREEN,
            TagKind.REPLACE: self.YELLOW,
        }

        return f"{colors[tag]}{text}{self.RESET}"

    def style_sign(self, sign):
        colors = {
            "-": ("x", self.RED),
            "+": ("v", self.GREEN),
        }

        mark, color = colors[sign]

        return f"{color}{self.BOLD}{mark}{self.RESET}"
