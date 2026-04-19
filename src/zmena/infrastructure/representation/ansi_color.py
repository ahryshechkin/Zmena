from zmena.domain.types.tag import Tag


class ANSIColor:
    GRAY = "\033[38;5;250m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    def style_text(self, tag, text):
        colors = {
            Tag.DELETE: self.RED,
            Tag.EQUAL: self.GRAY,
            Tag.INSERT: self.GREEN,
            Tag.REPLACE: self.YELLOW,
        }

        return f"{colors[tag]}{text}{self.RESET}"

    def style_sign(self, sign):
        colors = {
            "-": ("x", self.RED),
            "+": ("v", self.GREEN),
        }

        mark, color = colors[sign]

        return f"{color}{self.BOLD}{mark}{self.RESET}"
