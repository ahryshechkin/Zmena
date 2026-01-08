from constant import Color, Tag
from difflib import SequenceMatcher
from modules.brick import Brick
from modules.lexeme import Lexeme


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
            print(tag, slo, shi, tlo, thi)
            if tag == Tag.EQUAL:
                for idx in range(shi - slo):
                    left_lineno = slo + idx + 1
                    left_line = src[slo + idx]
                    right_lineno = tlo + idx + 1
                    right_line = trg[tlo + idx]
                    self.show_line(tag, left_lineno, left_line, right_lineno, right_line, "")
            elif tag == Tag.REPLACE:
                left_range = shi - slo
                right_range = thi - tlo
                max_range = max(left_range, right_range)
                for idx in range(max_range):
                    if idx < left_range:
                        left_lineno = slo + idx + 1
                        left_line = src[slo + idx]
                        self.bricks.append(Brick(tag, "L", left_lineno, Lexeme(left_line)))
                    else:
                        left_lineno = ""
                        left_line = ""
                    if idx < right_range:
                        right_lineno = tlo + idx + 1
                        right_line = trg[tlo + idx]
                        self.bricks.append(Brick(tag, "R", right_lineno, Lexeme(right_line)))
                    else:
                        right_lineno = ""
                        right_line = ""
                    self.show_line(tag, left_lineno, left_line, right_lineno, right_line, right_range - left_range)
            elif tag == Tag.INSERT:
                for idx in range(thi - tlo):
                    right_lineno = tlo + idx + 1
                    right_line = trg[tlo + idx]
                    self.bricks.append(Brick(tag, "R", right_lineno, Lexeme(right_line)))
                    self.show_line(tag, "", "", right_lineno, right_line, "")
            elif tag == Tag.DELETE:
                for idx in range(shi - slo):
                    left_lineno = slo + idx + 1
                    left_line = src[slo + idx]
                    self.bricks.append(Brick(tag, left_lineno, "L", Lexeme(left_line)))
                    self.show_line(tag, left_lineno, left_line, "", "", "")


    def print_header(self, name, desc):
        total_len = self.left_width + self.right_width - len(desc) + 28
        print(
            f"\n#### {name} - {desc} {'#' * total_len}\n"
            f"{'opcode':>7} | "
            f"{'lineno':>6} | {'source':<{self.left_width}} | "
            f"{'lineno':>6} | {'target':<{self.right_width}} | "
            f"{'counter':>7} | "
        )
        print(
            f"{'-' * 7}-+-{'-' * 6}-+-"
            f"{'-' * self.left_width}-+-{'-' * 6}-+-{'-' * self.right_width}-+-"
            f"{'-' * 7}-+"
        )


    def show_line(self, tag, left_lineno, left_line, right_lineno, right_line, cnt_ins):
        line = (
            f"{tag:>7} | "
            f"{left_lineno:>6} | {left_line:<{self.left_width}} | "
            f"{right_lineno:>6} | {right_line:<{self.right_width}} | "
            f"{cnt_ins:>7} | "
        )
        colored_line = self.colorize(tag, line)
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
