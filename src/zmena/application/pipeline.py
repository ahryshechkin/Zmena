from zmena.domain import (
    BrickService,
    ComponentService,
    Decision,
)
from zmena.domain.heuristics.compatibility import HeuristicCompatibility
from zmena.domain.heuristics.name import HeuristicName
from zmena.domain.heuristics.position import HeuristicPosition
from zmena.domain.heuristics.signature import HeuristicSignature
from zmena.domain.model.brick_bundle import BrickBundle
from zmena.domain.services.hypothesis_service import HypothesisService
from zmena.domain.services.rule_registry import RuleRegistry


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def run(self):
        brick_service = BrickService()
        bricks = brick_service.build(self.before, self.after)

        registry = RuleRegistry()
        bundle = BrickBundle(bricks)

        hypothesis_service = HypothesisService(registry)
        hypotheses = hypothesis_service.propose(bundle)

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
