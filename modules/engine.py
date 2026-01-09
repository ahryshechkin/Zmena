from constant import Tag
from difflib import SequenceMatcher
from modules.brick import LeftBrick, RightBrick
from modules.hunk import Hunk
from modules.span import Span
from modules.visualizer import Visualizer


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.bricks = list()


    def run(self, name, desc, src, trg):
        self.sm.set_seqs(src, trg)

        left_width = len(max(src, key=len, default=None))
        right_width = len(max(trg, key=len, default=None))
        visualizer = Visualizer(left_width, right_width)

        visualizer.print_header(name, desc)
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            # print(tag, slo, shi, tlo, thi)
            left = Span(src, slo, shi)
            right = Span(trg, tlo, thi)
            hunk = Hunk(tag, left, right)
            if tag == Tag.EQUAL:
                for idx in range(hunk.left_range()):
                    visualizer.show_line(idx, hunk)
            elif tag == Tag.REPLACE:
                for idx in range(hunk.height()):
                    visualizer.show_line(idx, hunk)
                    if idx < hunk.left_range():
                        brick = LeftBrick(idx, hunk)
                        self.bricks.append(brick)
                    if idx < hunk.right_range():
                        brick = RightBrick(idx, hunk)
                        self.bricks.append(brick)
            elif tag == Tag.INSERT:
                for idx in range(hunk.right_range()):
                    visualizer.show_line(idx, hunk)
                    brick = RightBrick(idx, hunk)
                    self.bricks.append(brick)
            elif tag == Tag.DELETE:
                for idx in range(hunk.left_range()):
                    visualizer.show_line(idx, hunk)
                    brick = LeftBrick(idx, hunk)
                    self.bricks.append(brick)
