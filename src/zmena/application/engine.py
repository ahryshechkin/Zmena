from collections import defaultdict
from difflib import SequenceMatcher

from zmena.domain import BrickLeft, BrickRight, Component, Hunk, Span, Tag


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

    def build_components(self, hypotheses):
        components = []

        brick_to_hypotheses = defaultdict(set)
        for hypothesis in hypotheses:
            brick_to_hypotheses[hypothesis.left].add(hypothesis)
            brick_to_hypotheses[hypothesis.right].add(hypothesis)

        visited_bricks = set()
        for brick in brick_to_hypotheses:
            if brick in visited_bricks:
                continue

            component = Component()
            stack = [brick]

            while stack:
                current_brick = stack.pop()
                if current_brick in visited_bricks:
                    continue
                visited_bricks.add(current_brick)
                for hypothesis in brick_to_hypotheses[current_brick]:
                    component.add(hypothesis)
                    if current_brick == hypothesis.left:
                        neighbor = hypothesis.right
                    else:
                        neighbor = hypothesis.left
                    stack.append(neighbor)

            components.append(component)

        return components
