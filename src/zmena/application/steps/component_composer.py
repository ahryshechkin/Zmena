from collections import defaultdict

from zmena.domain.model.component import Component


class ComponentComposer:
    def __init__(self, hypotheses):
        self.hypotheses = hypotheses

    def __repr__(self):
        return f"ComponentComposer(hypotheses={len(self.hypotheses)})"

    def compose(self):
        fragment_to_hypotheses = defaultdict(set)
        for hypothesis in self.hypotheses:
            left, right = hypothesis.key()
            fragment_to_hypotheses[left].add(hypothesis)
            fragment_to_hypotheses[right].add(hypothesis)

        components = []
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
                    neighbor = hypothesis.neighbor(current_fragment)
                    stack.append(neighbor)

            components.append(component)

        return components
