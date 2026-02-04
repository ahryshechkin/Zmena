class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        scores = dict()
        for link in self.component.links:
            score = 0
            for heuristic in self.heuristics:
                score += heuristic.score(link)
            scores[link] = score

        return scores
