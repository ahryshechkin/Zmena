from zmena.application.steps.component_service import ComponentService
from zmena.application.steps.decision_service import DecisionService
from zmena.application.steps.fragment_service import FragmentService
from zmena.application.steps.hypothesis_service import HypothesisService
from zmena.domain.model.fragment_bundle import FragmentBundle
from zmena.domain.services.heuristic_registry import HeuristicRegistry
from zmena.domain.services.rule_registry import RuleRegistry


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def run(self):
        fragment_service = FragmentService()
        fragments = fragment_service.build(self.before, self.after)

        bundle = FragmentBundle(fragments)
        hypothesis_service = HypothesisService(RuleRegistry())
        hypotheses = hypothesis_service.propose(bundle)

        component_service = ComponentService(hypotheses)
        components = component_service.compose()

        decision_service = DecisionService(HeuristicRegistry())
        decisions = decision_service.decide(components)

        return {
            "fragments": fragments,
            "hypotheses": hypotheses,
            "components": components,
            "decisions": decisions,
        }
