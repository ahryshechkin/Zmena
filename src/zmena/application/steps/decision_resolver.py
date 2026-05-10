from zmena.domain.model.decision import Decision
from zmena.domain.presets.heuristics import HeuristicPreset


class DecisionResolver:
    def __init__(self):
        self.preset = HeuristicPreset()

    def __repr__(self):
        return "DecisionResolver(preset=heuristics)"

    def resolve(self, components):
        decisions = []
        for component in components:
            decision = Decision(component, self.preset)
            decisions.append(decision)

        return decisions
