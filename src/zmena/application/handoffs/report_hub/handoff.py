from zmena.application.handoffs.report_hub.bridges.component import ComponentBridge
from zmena.application.handoffs.report_hub.bridges.decision import DecisionBridge
from zmena.application.handoffs.report_hub.bridges.fragment import FragmentBridge
from zmena.application.handoffs.report_hub.bridges.hypothesis import HypothesisBridge
from zmena.application.handoffs.report_hub.bridges.link import LinkBridge
from zmena.application.messages.inbound.report_hub import ReportHubInboundMessage


class ReportHubHandoff:
    def __init__(self, kind, scenario, message):
        self.kind = kind
        self.scenario = scenario
        self.message = message

    def __repr__(self):
        return "ReportHubHandoff(messages=sce,sei)"

    def prepare(self):
        fragment_bridge = FragmentBridge()
        hypothesis_bridge = HypothesisBridge(fragment_bridge)
        component_bridge = ComponentBridge(fragment_bridge, hypothesis_bridge)
        decision_bridge = DecisionBridge(LinkBridge(fragment_bridge))

        fragments = [fragment_bridge.translate(fragment) for fragment in self.message.fragments]
        hypotheses = [
            hypothesis_bridge.translate(hypothesis) for hypothesis in self.message.hypotheses
        ]
        components = [
            component_bridge.translate(component) for component in self.message.components
        ]
        decisions = [decision_bridge.translate(decision) for decision in self.message.decisions]

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
