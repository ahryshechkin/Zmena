from zmena.application.handoffs.report_hub.bridges.component import ComponentBridge
from zmena.application.handoffs.report_hub.bridges.decision import DecisionBridge
from zmena.application.handoffs.report_hub.bridges.fragment import FragmentBridge
from zmena.application.handoffs.report_hub.bridges.hypothesis import HypothesisBridge
from zmena.application.handoffs.report_hub.bridges.link import LinkBridge
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
        component_bridge = ComponentBridge(fragment_bridge, hypothesis_bridge)
        decision_bridge = DecisionBridge(LinkBridge(fragment_bridge))
        fragment_snapshots = [fragment_bridge.translate(fragment) for fragment in fragments]
        hypothesis_snapshots = [
            hypothesis_bridge.translate(hypothesis) for hypothesis in hypotheses
        ]
        component_snapshots = [component_bridge.translate(component) for component in components]
        decision_snapshots = [decision_bridge.translate(decision) for decision in decisions]

        return SemanticEngineOutboundMessage(
            fragments=fragment_snapshots,
            hypotheses=hypothesis_snapshots,
            components=component_snapshots,
            decisions=decision_snapshots,
        )
