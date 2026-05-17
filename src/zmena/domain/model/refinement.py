from zmena.domain.model.context import Context


class Refinement:
    def __init__(self, heuristics):
        self.heuristics = heuristics

    def __repr__(self):
        return "Refinement"

    def reassess(self, links):
        context = Context(links)

        links_for_reassessment = context.links_for_reassessment()
        for link in links_for_reassessment:
            for heuristic in self.heuristics:
                for evidence in heuristic.evaluate(link, context):
                    link.add_evidence(evidence)

        return links_for_reassessment
