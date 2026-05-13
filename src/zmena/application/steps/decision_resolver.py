from zmena.domain.model.decision import Decision
from zmena.domain.model.refinement import Refinement
from zmena.domain.presets.heuristics import HeuristicPreset


class DecisionResolver:
    def __init__(self):
        self.preset = HeuristicPreset()

    def __repr__(self):
        return "DecisionResolver(preset=heuristics)"

    def resolve(self, components):
        decisions = []
        for component in components:
            initial_links = component.assess(self.preset.local())
            refinement = Refinement(initial_links)
            refined_links = refinement.reassess(self.preset.overall())
            decision = Decision(refined_links)
            decisions.append(decision)

        return decisions
