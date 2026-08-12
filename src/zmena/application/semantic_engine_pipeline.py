from zmena.application.semantic_engine_result import SemanticEngineResult
from zmena.domain.semantic_engine.core.fragment_bundle import FragmentBundle
from zmena.domain.semantic_engine.steps.component_composer import ComponentComposer
from zmena.domain.semantic_engine.steps.decision_resolver import DecisionResolver
from zmena.domain.semantic_engine.steps.fragment_builder import FragmentBuilder
from zmena.domain.semantic_engine.steps.hypothesis_proposer import HypothesisProposer


class SemanticEnginePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "AnalysisPipeline"

    def run(self):
        fragment_builder = FragmentBuilder()
        fragments = fragment_builder.build(self.message.before, self.message.after)

        bundle = FragmentBundle(fragments)
        hypothesis_proposer = HypothesisProposer(bundle)
        hypotheses = hypothesis_proposer.propose()

        component_composer = ComponentComposer(hypotheses)
        components = component_composer.compose()

        decision_resolver = DecisionResolver(components)
        decisions = decision_resolver.resolve()

        return SemanticEngineResult(
            fragments=fragments, hypotheses=hypotheses, components=components, decisions=decisions
        )
