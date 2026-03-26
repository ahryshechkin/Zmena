from zmena.domain import (
    BrickService,
    ComponentService,
    Decision,
    HeuristicCompatibility,
    HeuristicName,
    HeuristicPosition,
    HeuristicSignature,
)
from zmena.domain.model.brick_bundle import BrickBundle
from zmena.domain.services.hypothesis_service import HypothesisService


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def run(self):
        brick_service = BrickService()
        bricks = brick_service.build(self.before, self.after)

        bundle = BrickBundle(bricks)

        hypothesis_service = HypothesisService(bundle)
        hypotheses = hypothesis_service.propose()

        component_service = ComponentService(hypotheses)
        components = component_service.compose()

        selected_links, all_links = [], []
        heuristics = [
            HeuristicCompatibility(),
            HeuristicName(),
            HeuristicPosition(),
            HeuristicSignature(),
        ]
        for component in components:
            all_links.append(component.assess(heuristics))
            decision = Decision(component, heuristics)
            selected_links.append(decision.make())

        return {
            "bricks": bricks,
            "hypotheses": hypotheses,
            "components": components,
            "all_links": all_links,
            "selected_links": selected_links,
        }
