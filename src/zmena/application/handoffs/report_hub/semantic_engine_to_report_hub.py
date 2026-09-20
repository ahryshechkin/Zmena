from zmena.application.handoffs.report_hub.bridges.component import ComponentBridge
from zmena.application.handoffs.report_hub.bridges.decision import DecisionBridge
from zmena.application.handoffs.report_hub.bridges.fragment import FragmentBridge
from zmena.application.handoffs.report_hub.bridges.hypothesis import HypothesisBridge
from zmena.application.handoffs.report_hub.bridges.link import LinkBridge
from zmena.application.messages.inbound.report_hub import ReportHubInboundMessage


class SemanticEngineToReportHubHandoff:
    def __init__(self, kind, scenario, seo_message):
        self.kind = kind
        self.scenario = scenario
        self.seo_message = seo_message

    def __repr__(self):
        return "SemanticEngineToReportHubHandoff(messages=sce,seo)"

    def prepare(self):
        fragment_bridge = FragmentBridge()
        hypothesis_bridge = HypothesisBridge(fragment_bridge)
        component_bridge = ComponentBridge(fragment_bridge, hypothesis_bridge)
        decision_bridge = DecisionBridge(LinkBridge(fragment_bridge))

        fragments = [fragment_bridge.translate(fragment) for fragment in self.seo_message.fragments]
        hypotheses = [
            hypothesis_bridge.translate(hypothesis) for hypothesis in self.seo_message.hypotheses
        ]
        components = [
            component_bridge.translate(component) for component in self.seo_message.components
        ]
        decisions = [decision_bridge.translate(decision) for decision in self.seo_message.decisions]

        return ReportHubInboundMessage(
            kind=self.kind,
            label=self.scenario.sce_id,
            name=self.scenario.name,
            before=self.scenario.before.splitlines(),
            after=self.scenario.after.splitlines(),
            fragments=fragments,
            hypotheses=hypotheses,
            components=components,
            decisions=decisions,
        )
