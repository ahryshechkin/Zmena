class Refinement:
    def __init__(self, heuristics):
        self.heuristics = heuristics

    def __repr__(self):
        return "Refinement"

    def reassess(self, links):
        for link in links:
            for heuristic in self.heuristics:
                for evidence in heuristic.evaluate(link, links):
                    link.add_evidence(evidence)

        return links
