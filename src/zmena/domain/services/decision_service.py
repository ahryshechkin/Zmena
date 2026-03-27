from zmena.domain.model.decision import Decision


class DecisionService:
    def __init__(self, registry):
        self.registry = registry

    def decide(self, components):
        links = []
        for component in components:
            decision = Decision(component, self.registry.default_heuristics())
            links.append(decision.make())

        return links
