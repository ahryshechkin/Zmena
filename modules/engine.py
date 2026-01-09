from constant import Color, Tag
from difflib import SequenceMatcher
from modules.brick import LeftBrick, RightBrick
from modules.hunk import Hunk
from modules.lexeme import Lexeme
from modules.span import Span


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.left_width = None
        self.right_width = None
        self.bricks = list()


    def set_width(self, src, trg):
        self.left_width = len(max(src, key=len, default=None))
        self.right_width = len(max(trg, key=len, default=None))


    def run(self, name, desc, src, trg):
        self.sm.set_seqs(src, trg)

        self.print_header(name, desc)
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            # print(tag, slo, shi, tlo, thi)
            left = Span(src, slo, shi)
            right = Span(trg, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.EQUAL:
                for idx in range(hunk.left_range()):
                    self.show_line(idx, hunk)
            elif tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    if idx < hunk.left_range():
                        brick = LeftBrick(idx, hunk)
                        self.bricks.append(brick)
                    if idx < hunk.right_range():
                        brick = RightBrick(idx, hunk)
                        self.bricks.append(brick)
                    self.show_line(idx, hunk)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    brick = RightBrick(idx, hunk)
                    self.bricks.append(brick)
                    self.show_line(idx, hunk)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    brick = LeftBrick(idx, hunk)
                    self.bricks.append(brick)
                    self.show_line(idx, hunk)


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
