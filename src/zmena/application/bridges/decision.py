from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.semantic_engine.snapshots.decision import DecisionSnapshot


class DecisionBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.DECISION)
        self.bridge = bridge

    def translate(self, decision):
        candidates = [self.bridge.translate(link) for link in decision.candidates()]
        winners = [self.bridge.translate(link) for link in decision.winners()]

        return DecisionSnapshot(candidates=candidates, winners=winners)
