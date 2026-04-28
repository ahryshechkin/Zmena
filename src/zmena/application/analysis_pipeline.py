from zmena.application.analysis_result import AnalysisResult
from zmena.application.presets.heuristics import HeuristicPreset
from zmena.application.presets.rules import RulePreset
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

        rule_preset = RulePreset()
        bundle = FragmentBundle(fragments)
        hypothesis_proposer = HypothesisProposer(rule_preset.default())
        hypotheses = hypothesis_proposer.propose(bundle)

        component_composer = ComponentComposer(hypotheses)
        components = component_composer.compose()

        heuristic_preset = HeuristicPreset()
        decision_resolver = DecisionResolver(heuristic_preset.default())
        decisions = decision_resolver.resolve(components)

        return AnalysisResult(fragments, hypotheses, components, decisions)
