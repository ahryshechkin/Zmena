from constant import Color, Tag


class Visualizer:
    def __init__(self, left_width, right_width):
        self.left_width = left_width
        self.right_width = right_width


    def print_header(self, name, desc):
        total_len = self.left_width + self.right_width - len(desc) + 17
        print(
            f"\n#### {name} - {desc} {'#' * total_len}\n"
            f"{'opcode':>7} | "
            f"{'lineno':>6} | {'left':<{self.left_width}} | "
            f"{'lineno':>6} | {'right':<{self.right_width}} | "
        )
        print(
            f"{'-' * 7}-+-{'-' * 6}-+-"
            f"{'-' * self.left_width}-+-{'-' * 6}-+-{'-' * self.right_width}-+"
        )


    def show_line(self, offset, hunk):
        line = (
            f"{hunk.tag():>7} | "
            f"{hunk.left_lineno(offset):>6} | {hunk.left_line(offset):<{self.left_width}} | "
            f"{hunk.right_lineno(offset):>6} | {hunk.right_line(offset):<{self.right_width}} | "
        )
        colored_line = self.colorize(hunk.tag(), line)
        print(colored_line)


    def colorize(self, tag, text):
        colors = {
            Tag.DELETE: Color.RED,
            Tag.EQUAL: Color.GRAY,
            Tag.INSERT: Color.GREEN,
            Tag.REPLACE: Color.YELLOW,
        }

        color = colors[tag].value

        return f"{color}{text}{Color.RESET.value}"
