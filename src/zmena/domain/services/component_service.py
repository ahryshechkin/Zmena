from collections import defaultdict

from zmena.domain.model.component import Component


class ComponentService:
    def __init__(self, hypotheses):
        self.hypotheses = hypotheses

    def __repr__(self):
        return f"ComponentService(hypotheses={len(self.hypotheses)})"

    def compose(self):
        components = []

        fragment_to_hypotheses = defaultdict(set)
        for hypothesis in self.hypotheses:
            fragment_to_hypotheses[hypothesis.left].add(hypothesis)
            fragment_to_hypotheses[hypothesis.right].add(hypothesis)

        visited_fragments = set()
        for fragment in fragment_to_hypotheses:
            if fragment in visited_fragments:
                continue

            component = Component()

            stack = [fragment]
            while stack:
                current_fragment = stack.pop()
                if current_fragment in visited_fragments:
                    continue
                visited_fragments.add(current_fragment)
                for hypothesis in fragment_to_hypotheses[current_fragment]:
                    component.add(hypothesis)
                    if current_fragment == hypothesis.left:
                        neighbor = hypothesis.right
                    else:
                        neighbor = hypothesis.left
                    stack.append(neighbor)

            components.append(component)

        return components
