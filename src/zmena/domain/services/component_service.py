from collections import defaultdict

from zmena.domain.model.component import Component


class ComponentService:
    def __init__(self, hypotheses):
        self.hypotheses = hypotheses

    def compose(self):
        components = []

        brick_to_hypotheses = defaultdict(set)
        for hypothesis in self.hypotheses:
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
