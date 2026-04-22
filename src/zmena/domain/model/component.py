from zmena.domain.model.link import Link


class Component:
    def __init__(self):
        self.fragments = set()
        self.hypotheses = set()

    def __repr__(self):
        return f"Component(fragments={len(self.fragments)},hypotheses={len(self.hypotheses)})"

    def add(self, hypothesis):
        left, right = hypothesis.key()
        self.fragments.add(left)
        self.fragments.add(right)
        self.hypotheses.add(hypothesis)

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
