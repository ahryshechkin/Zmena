from difflib import SequenceMatcher

from zmena.domain.model.brick.left import BrickLeft
from zmena.domain.model.brick.right import BrickRight
from zmena.domain.model.hunk import Hunk
from zmena.domain.model.span import Span
from zmena.domain.types.tag import Tag


class BrickService:
    def __init__(self):
        self.sm = SequenceMatcher()

    def __repr__(self):
        return "BrickService"

    def build(self, before, after):
        self.sm.set_seqs(before, after)

        bricks = []
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(before, slo, shi)
            right = Span(after, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    if idx < hunk.left_range():
                        brick = BrickLeft(idx, hunk)
                        bricks.append(brick)
                    if idx < hunk.right_range():
                        brick = BrickRight(idx, hunk)
                        bricks.append(brick)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    brick = BrickRight(idx, hunk)
                    bricks.append(brick)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    brick = BrickLeft(idx, hunk)
                    bricks.append(brick)

        return bricks
