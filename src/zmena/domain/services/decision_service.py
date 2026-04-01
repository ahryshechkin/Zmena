from zmena.domain.model.decision import Decision


class DecisionService:
    def __init__(self, registry):
        self.registry = registry

    def __repr__(self):
        return "DecisionService(registry=heuristic)"

    def decide(self, components):
        decisions = []
        for component in components:
            decision = Decision(component, self.registry.default_heuristics())
            decisions.append(decision)

        return decisions
