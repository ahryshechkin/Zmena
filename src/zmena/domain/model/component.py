from zmena.domain.model.link import Link


class Component:
    def __init__(self):
        self.hypotheses = set()
        self.bricks = set()

    def __repr__(self):
        return f"Component(hypotheses={len(self.hypotheses)},bricks={len(self.bricks)})"

    def add(self, hypothesis):
        self.hypotheses.add(hypothesis)
        self.bricks.add(hypothesis.left)
        self.bricks.add(hypothesis.right)

    def assess(self, heuristics):
        links = {}

        for hypothesis in self.hypotheses:
            key = hypothesis.key()

            link = links.get(key)
            if link is None:
                link = Link(hypothesis)
                links[key] = link

            for heuristic in heuristics:
                for evidence in heuristic.evaluate(hypothesis):
                    link.add_evidence(evidence)

        return list(links.values())
