from zmena.domain.model.decision import Decision


class DecisionResolver:
    def __init__(self, registry):
        self.registry = registry

    def __repr__(self):
        return "DecisionResolver(registry=heuristic)"

    def resolve(self, components):
        decisions = []
        for component in components:
            decision = Decision(component, self.registry.default_heuristics())
            decisions.append(decision)

        return decisions
