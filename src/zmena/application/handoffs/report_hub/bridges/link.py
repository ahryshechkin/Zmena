from zmena.application.bridges.bridge import Bridge
from zmena.application.handoffs.report_hub.snapshots.link import LinkSnapshot
from zmena.application.kinds.bridge import BridgeKind


class LinkBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.LINK)
        self.bridge = bridge

    def translate(self, link):
        left, right = link.fragments()

        return LinkSnapshot(
            score=link.score(),
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
            evidences=link.evidences,
        )
