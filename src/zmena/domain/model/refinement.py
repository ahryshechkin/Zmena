from zmena.domain.model.context import Context


class Refinement:
    def __init__(self, lenses):
        self.lenses = lenses

    def __repr__(self):
        return "Refinement"

    def reassess(self, links):
        context = Context(links)

        working_links = context.cloned_links()
        for link in working_links:
            for lens in self.lenses:
                for evidence in lens.evaluate(link, context):
                    link.add_evidence(evidence)

        return working_links
