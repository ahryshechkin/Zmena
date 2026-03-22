from zmena.domain.model.link.scored_link import ScoredLink


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
