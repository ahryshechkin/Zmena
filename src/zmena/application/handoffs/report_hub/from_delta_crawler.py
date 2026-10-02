from zmena.application.handoffs.report_hub.bridges.component import ComponentBridge
from zmena.application.handoffs.report_hub.bridges.decision import DecisionBridge
from zmena.application.handoffs.report_hub.bridges.evidence import EvidenceBridge
from zmena.application.handoffs.report_hub.bridges.fragment import FragmentMint
from zmena.application.handoffs.report_hub.bridges.hypothesis import HypothesisBridge
from zmena.application.handoffs.report_hub.bridges.link import LinkBridge
from zmena.application.handoffs.report_hub.messages.inbound import ReportHubInboundMessage


class DeltaCrawlerToReportHubHandoff:
    def __init__(self, dco_message, sio_message, seo_message):
        self.dco_message = dco_message
        self.sio_message = sio_message
        self.seo_message = seo_message

    def __repr__(self):
        return "DeltaCrawlerToReportHubHandoff(messages=dco,sio,seo)"

    def prepare(self):
        fragment_bridge = FragmentMint()
        hypothesis_bridge = HypothesisBridge(fragment_bridge)
        evidence_bridge = EvidenceBridge()
        component_bridge = ComponentBridge(fragment_bridge, hypothesis_bridge)
        decision_bridge = DecisionBridge(LinkBridge(fragment_bridge, evidence_bridge))

        fragments = [fragment_bridge.translate(fragment) for fragment in self.seo_message.fragments]
        hypotheses = [
            hypothesis_bridge.translate(hypothesis) for hypothesis in self.seo_message.hypotheses
        ]
        components = [
            component_bridge.translate(component) for component in self.seo_message.components
        ]
        decisions = [decision_bridge.translate(decision) for decision in self.seo_message.decisions]
        statements = []

        return ReportHubInboundMessage(
            kind="CMT",
            label=self.dco_message.cmt_id,
            name=self.dco_message.name,
            before=self.sio_message.before,
            after=self.sio_message.after,
            fragments=fragments,
            hypotheses=hypotheses,
            components=components,
            decisions=decisions,
            statements=statements,
        )
