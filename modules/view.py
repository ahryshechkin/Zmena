from difflib import SequenceMatcher
from modules.constant import Color, Tag
from modules.hunk import Hunk
from modules.span import Span


class View:
    def __init__(self, sample):
        self.name = sample["name"]
        self.desc = sample["desc"]
        self.src = sample["src"].strip().splitlines()
        self.trg = sample["trg"].strip().splitlines()
        self.left_width = len(max(self.src, key=len, default=None))
        self.right_width = len(max(self.trg, key=len, default=None))
        self.sm = SequenceMatcher()


    def show_report(self):
        self.sm.set_seqs(self.src, self.trg)

        self.print_report_header()
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(self.src, slo, shi)
            right = Span(self.trg, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.EQUAL:
                for idx in range(hunk.left_range()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    self.print_report_line(idx, hunk)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    self.print_report_line(idx, hunk)


    def print_report_header(self):
        total_len = self.left_width + self.right_width - len(self.desc) + 28

        print(
            f"\n#### {self.name} - {self.desc} {'#' * total_len}\n"
            f"{'action':>7} | {'opcode':>8} | "
            f"{'lineno':>6} | {'left':<{self.left_width}} | "
            f"{'lineno':>6} | {'right':<{self.right_width}} | "
        )
        print(
            f"{'-' * 7}-+-{'-' * 8}-+-{'-' * 6}-+-"
            f"{'-' * self.left_width}-+-{'-' * 6}-+-{'-' * self.right_width}-+"
        )


    def print_report_line(self, offset, hunk):
        line = (
            f"{hunk.tag():>7} | {hunk.uid():>8} | "
            f"{hunk.left_lineno(offset):>6} | {hunk.left_line(offset):<{self.left_width}} | "
            f"{hunk.right_lineno(offset):>6} | {hunk.right_line(offset):<{self.right_width}} | "
        )

        print(self.colorize(hunk.tag(), line))


    def colorize(self, tag, text):
        colors = {
            Tag.DELETE: Color.RED,
            Tag.EQUAL: Color.GRAY,
            Tag.INSERT: Color.GREEN,
            Tag.REPLACE: Color.YELLOW,
        }

        color = colors[tag].value

        return f"{color}{text}{Color.RESET.value}"


    def show_bricks(self, bricks):
        print(
            f"\n{'#' * 77} \n"
            f"{'tag':>7} | {'side':>4} | {'segment':<8} | {'position':>8} | "
            f"{'name':<7} | {'type':<13} | {'constraint':<10} |"
        )
        print(
            f"{'-' * 7}-+-{'-' * 4}-+-{'-' * 8}-+-"
            f"{'-' * 8}-+-{'-' * 7}-+-{'-' * 13}-+-{'-' * 10}-+"
        )

        for brick in bricks:
            print(brick)