class Decision:
    def __init__(self, component, heuristics):
        self.component = component
        self.heuristics = heuristics


    def make(self):
        result = dict()

        for link in self.component.links:
            scores = list()
            for heuristic in self.heuristics:
                score = heuristic.score(link)
                scores.append(score)
            result[link] = scores

        return result

