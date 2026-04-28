from zmena.domain.model.decision import Decision


class DecisionResolver:
    def __init__(self, heuristics):
        self.heuristics = heuristics

    def __repr__(self):
        return "DecisionResolver(preset=heuristics)"

    def resolve(self, components):
        decisions = []
        for component in components:
            decision = Decision(component, self.heuristics)
            decisions.append(decision)

        return decisions
