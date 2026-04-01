from zmena.domain.model.brick_bundle import BrickBundle
from zmena.domain.services.brick_service import BrickService
from zmena.domain.services.component_service import ComponentService
from zmena.domain.services.decision_service import DecisionService
from zmena.domain.services.heuristic_registry import HeuristicRegistry
from zmena.domain.services.hypothesis_service import HypothesisService
from zmena.domain.services.rule_registry import RuleRegistry


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def run(self):
        brick_service = BrickService()
        bricks = brick_service.build(self.before, self.after)

        bundle = BrickBundle(bricks)
        hypothesis_service = HypothesisService(RuleRegistry())
        hypotheses = hypothesis_service.propose(bundle)

        component_service = ComponentService(hypotheses)
        components = component_service.compose()

        decision_service = DecisionService(HeuristicRegistry())
        decisions = decision_service.decide(components)

        return {
            "bricks": bricks,
            "hypotheses": hypotheses,
            "components": components,
            "decisions": decisions,
        }
