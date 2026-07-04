from zmena.domain.semantic_engine.model.decision import Decision
from zmena.domain.semantic_engine.model.refinement import Refinement
from zmena.domain.semantic_engine.presets.lenses import LensPreset


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
            locally_accessed = component.assess()
            globally_reassessed = refinement.reassess(locally_accessed)
            decision = Decision(globally_reassessed)
            decisions.append(decision)

        return decisions
