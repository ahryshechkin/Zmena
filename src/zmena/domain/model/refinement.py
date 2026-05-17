from zmena.domain.model.context import Context


class Refinement:
    def __init__(self, lenses):
        self.lenses = lenses

    def __repr__(self):
        return "Refinement"

    def reassess(self, links):
        context = Context(links)

        links_for_reassessment = context.links_for_reassessment()
        for link in links_for_reassessment:
            for lens in self.lenses:
                for evidence in lens.evaluate():
                    link.add_evidence(evidence)

        return links_for_reassessment
