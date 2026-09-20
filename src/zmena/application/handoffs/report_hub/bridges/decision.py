from zmena.application.handoffs.report_hub.bridges.bridge import Bridge
from zmena.application.handoffs.report_hub.snapshots.decision import DecisionSnapshot
from zmena.application.kinds.bridge import BridgeKind


class DecisionBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.DECISION)
        self.bridge = bridge

    def translate(self, decision):
        candidates = [self.bridge.translate(link) for link in decision.candidates()]
        winners = [self.bridge.translate(link) for link in decision.winners()]

        return DecisionSnapshot(candidates=candidates, winners=winners)
