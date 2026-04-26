from zmena.application.steps.component_composer import ComponentComposer
from zmena.application.steps.decision_resolver import DecisionResolver
from zmena.application.steps.fragment_builder import FragmentBuilder
from zmena.application.steps.hypothesis_proposer import HypothesisProposer
from zmena.domain.model.fragment_bundle import FragmentBundle
from zmena.domain.services.heuristic_registry import HeuristicRegistry
from zmena.domain.services.rule_registry import RuleRegistry


class Pipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def run(self):
        fragment_builder = FragmentBuilder()
        fragments = fragment_builder.build(self.before, self.after)

        bundle = FragmentBundle(fragments)
        hypothesis_proposer = HypothesisProposer(RuleRegistry())
        hypotheses = hypothesis_proposer.propose(bundle)

        component_composer = ComponentComposer(hypotheses)
        components = component_composer.compose()

        decision_resolver = DecisionResolver(HeuristicRegistry())
        decisions = decision_resolver.resolve(components)

        return {
            "fragments": fragments,
            "hypotheses": hypotheses,
            "components": components,
            "decisions": decisions,
        }
