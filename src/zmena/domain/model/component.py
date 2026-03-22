from zmena.domain.model.link.scored_link import ScoredLink
from zmena.domain.model.link2 import Link


class Component:
    def __init__(self):
        self.hypotheses = set()
        self.bricks = set()

    def add(self, hypothesis):
        self.hypotheses.add(hypothesis)
        self.bricks.add(hypothesis.left)
        self.bricks.add(hypothesis.right)

    def assess(self, heuristics):
        scored_links = []

        for hypothesis in self.hypotheses:
            score = 0
            for heuristic in heuristics:
                for evidence in heuristic.evaluate(hypothesis):
                    score += evidence.score
            scored_links.append(ScoredLink(score, hypothesis))

        return scored_links

    def assess2(self, heuristics):
        link_index = {}

        for hypothesis in self.hypotheses:
            key = hypothesis.key()

            link = link_index.get(key)
            if link is None:
                link = Link(hypothesis)
                link_index[key] = link

            for heuristic in heuristics:
                for evidence in heuristic.evaluate(hypothesis):
                    link.add_evidence(evidence)

        return list(link_index.values())
