from collections import defaultdict
from difflib import SequenceMatcher

from domain import BrickLeft, BrickRight, Component, Hunk, Span, Tag


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.bricks = list()


    def build_bricks(self, src, trg):
        self.sm.set_seqs(src, trg)

        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            left = Span(src, slo, shi)
            right = Span(trg, tlo, thi)
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


    def build_components(self, links):
        components = list()

        brick_to_links = defaultdict(set)
        for link in links:
            brick_to_links[link.left].add(link)
            brick_to_links[link.right].add(link)


        visited_bricks = set()
        for brick in brick_to_links:
            if brick in visited_bricks:
                continue

            component = Component()
            stack = [brick]

            while stack:
                current_brick = stack.pop()
                if current_brick in visited_bricks:
                    continue
                visited_bricks.add(current_brick)
                for link in brick_to_links[current_brick]:
                    component.add(link)
                    if current_brick == link.left:
                        neighbor = link.right
                    else:
                        neighbor = link.left
                    stack.append(neighbor)

            components.append(component)

        return components
