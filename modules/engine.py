from constant import Tag
from difflib import SequenceMatcher


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.width = 30


    def run(self, src, trg):
        self.sm.set_seqs(src, trg)

        print(f"{'opcode':>7} | {'source':<{self.width}} | {'target'}")
        print(f"{'-' * 7}-+-{'-' * self.width}-+-{'-' * self.width}")
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            if tag == Tag.EQUAL:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    right = trg[tlo + idx]
                    self.transform_line(tag, left, right)
            elif tag == Tag.REPLACE:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    right = trg[tlo + idx]
                    self.transform_line(tag, left, right)
            elif tag == Tag.INSERT:
                for idx in range(thi - tlo):
                    right = trg[tlo + idx]
                    self.transform_line(tag, "", right)
            elif tag == Tag.DELETE:
                for idx in range(shi - slo):
                    left = src[slo + idx]
                    self.transform_line(tag, left, "")


    def transform_line(self, tag, left, right):
        print(f"{tag:>7} | {left:<{self.width}} | {right}")
