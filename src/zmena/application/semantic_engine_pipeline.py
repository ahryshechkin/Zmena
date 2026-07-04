from zmena.application.analysis_result import AnalysisResult
from zmena.application.steps.component_composer import ComponentComposer
from zmena.application.steps.decision_resolver import DecisionResolver
from zmena.application.steps.fragment_builder import FragmentBuilder
from zmena.application.steps.hypothesis_proposer import HypothesisProposer
from zmena.domain.semantic_engine.model.fragment_bundle import FragmentBundle


class SemanticEnginePipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "AnalysisPipeline"

    def run(self):
        fragment_builder = FragmentBuilder()
        fragments = fragment_builder.build(self.before, self.after)

        bundle = FragmentBundle(fragments)
        hypothesis_proposer = HypothesisProposer(bundle)
        hypotheses = hypothesis_proposer.propose()

        component_composer = ComponentComposer(hypotheses)
        components = component_composer.compose()

        decision_resolver = DecisionResolver(components)
        decisions = decision_resolver.resolve()

        return AnalysisResult(
            fragments=fragments, hypotheses=hypotheses, components=components, decisions=decisions
        )
