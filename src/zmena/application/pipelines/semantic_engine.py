from zmena.application.bridges.decision import DecisionBridge
from zmena.application.bridges.fragment import FragmentBridge
from zmena.application.bridges.hypothesis import HypothesisBridge
from zmena.application.bridges.link import LinkBridge
from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.messages.outbound.semantic_engine import SemanticEngineOutboundMessage
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.semantic_engine.core.fragment_bundle import FragmentBundle
from zmena.domain.semantic_engine.steps.component_composer import ComponentComposer
from zmena.domain.semantic_engine.steps.decision_resolver import DecisionResolver
from zmena.domain.semantic_engine.steps.fragment_builder import FragmentBuilder
from zmena.domain.semantic_engine.steps.hypothesis_proposer import HypothesisProposer


class SemanticEnginePipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.SEMANTIC_ENGINE)
        self.message = message

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

        fragment_bridge = FragmentBridge()
        hypothesis_bridge = HypothesisBridge(fragment_bridge)
        decision_bridge = DecisionBridge(LinkBridge(fragment_bridge))
        fragments_snap = [fragment_bridge.translate(fragment) for fragment in fragments]
        hypotheses_snap = [hypothesis_bridge.translate(hypothesis) for hypothesis in hypotheses]
        decisions_snap = [decision_bridge.translate(decision) for decision in decisions]

        return SemanticEngineOutboundMessage(
            fragments=fragments,
            fragments_snap=fragments_snap,
            hypotheses=hypotheses_snap,
            components=components,
            decisions=decisions,
            decisions_snap=decisions_snap,
        )
