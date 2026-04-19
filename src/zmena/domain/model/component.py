from zmena.domain.model.link import Link


class Component:
    def __init__(self):
        self.hypotheses = set()
        self.fragments = set()

    def __repr__(self):
        return f"Component(hypotheses={len(self.hypotheses)},fragments={len(self.fragments)})"

    def add(self, hypothesis):
        self.hypotheses.add(hypothesis)
        self.fragments.add(hypothesis.left)
        self.fragments.add(hypothesis.right)

    def assess(self, heuristics):
        links = {}

        for hypothesis in self.hypotheses:
            key = hypothesis.key()
            if key in links:
                continue

            link = Link(*key)
            for heuristic in heuristics:
                for evidence in heuristic.evaluate(hypothesis):
                    link.add_evidence(evidence)

            links[key] = link

        return list(links.values())
