from constant import Tag
from difflib import SequenceMatcher
from modules.brick import LeftBrick, RightBrick
from modules.hunk import Hunk
from modules.span import Span


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.bricks = list()


    def run(self, src, trg):
        self.sm.set_seqs(src, trg)

        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(src, slo, shi)
            right = Span(trg, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    if idx < hunk.left_range():
                        brick = LeftBrick(idx, hunk)
                        self.bricks.append(brick)
                    if idx < hunk.right_range():
                        brick = RightBrick(idx, hunk)
                        self.bricks.append(brick)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    brick = RightBrick(idx, hunk)
                    self.bricks.append(brick)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    brick = LeftBrick(idx, hunk)
                    self.bricks.append(brick)
