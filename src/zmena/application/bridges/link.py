from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.semantic_engine.snapshots.link import LinkSnapshot


class LinkBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.LINK)
        self.bridge = bridge

    def translate(self, link):
        left, right = link.fragments()

        return LinkSnapshot(
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
        )
