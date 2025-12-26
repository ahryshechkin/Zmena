from constant import Color, Tag
from difflib import SequenceMatcher


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.width = 30


    def run(self, src, trg):
        self.sm.set_seqs(src, trg)

        self.print_header()
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            if tag == Tag.EQUAL:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    right = trg[tlo + idx]
                    self.show_line(tag, left, right)
            elif tag == Tag.REPLACE:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    right = trg[tlo + idx]
                    self.show_line(tag, left, right)
            elif tag == Tag.INSERT:
                for idx in range(thi - tlo):
                    right = trg[tlo + idx]
                    self.show_line(tag, "", right)
            elif tag == Tag.DELETE:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    self.show_line(tag, left, "")


    def print_header(self):
        print(f"{'opcode':>7} | {'source':<{self.width}} | {'target'}")
        print(f"{'-' * 7}-+-{'-' * self.width}-+-{'-' * self.width}")


    def show_line(self, tag, left, right):
        line = f"{tag:>7} | {left:<{self.width}} | {right}"
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
