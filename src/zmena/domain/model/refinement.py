class Refinement:
    def __init__(self, links):
        self.links = links

    def __repr__(self):
        return f"Refinement(links={len(self.links)})"

    def reassess(self, heuristics):
        for link in self.links:
            for heuristic in heuristics:
                for evidence in heuristic.evaluate(link, self.links):
                    link.add_evidence(evidence)

        return self.links
