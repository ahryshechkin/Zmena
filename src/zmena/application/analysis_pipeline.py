from zmena.application.analysis_result import AnalysisResult
from zmena.application.presets.heuristic_registry import HeuristicRegistry
from zmena.application.presets.rule_registry import RuleRegistry
from zmena.application.steps.component_composer import ComponentComposer
from zmena.application.steps.decision_resolver import DecisionResolver
from zmena.application.steps.fragment_builder import FragmentBuilder
from zmena.application.steps.hypothesis_proposer import HypothesisProposer
from zmena.domain.model.fragment_bundle import FragmentBundle


class AnalysisPipeline:
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

        return AnalysisResult(fragments, hypotheses, components, decisions)
