from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.semantic_engine.snapshots.decision import DecisionSnapshot


class DecisionBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.DECISION)
        self.bridge = bridge

    def translate(self, decision):
        selected_links = [self.bridge.translate(link) for link in decision.winners()]

        return DecisionSnapshot(selected_links=selected_links)
