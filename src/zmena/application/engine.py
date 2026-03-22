from difflib import SequenceMatcher

from zmena.domain import BrickLeft, BrickRight, Hunk, Span, Tag


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.bricks = []

    def build_bricks(self, before, after):
        self.sm.set_seqs(before, after)

        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(before, slo, shi)
            right = Span(after, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    if idx < hunk.left_range():
                        brick = BrickLeft(idx, hunk)
                        self.bricks.append(brick)
                    if idx < hunk.right_range():
                        brick = BrickRight(idx, hunk)
                        self.bricks.append(brick)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    brick = BrickRight(idx, hunk)
                    self.bricks.append(brick)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    brick = BrickLeft(idx, hunk)
                    self.bricks.append(brick)
