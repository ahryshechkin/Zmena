from zmena.domain.model.decision import Decision
from zmena.domain.model.refinement import Refinement
from zmena.domain.presets.lenses import LensPreset


class DecisionResolver:
    def __init__(self, components):
        self.components = components
        self.preset = LensPreset()

    def __repr__(self):
        return f"DecisionResolver(components={len(self.components)})"

    def resolve(self):
        decisions = []

        refinement = Refinement(self.preset.default())
        for component in self.components:
            locally_scored_links = component.assess()
            globally_refined_links = refinement.reassess(locally_scored_links)
            decision = Decision(globally_refined_links)
            decisions.append(decision)

        return decisions
