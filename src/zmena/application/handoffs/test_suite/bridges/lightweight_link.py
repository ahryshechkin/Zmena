from zmena.application.handoffs.report_hub.bridges.bridge import Bridge
from zmena.application.handoffs.test_suite.snapshots.lightweight_link import LightweightLinkSnapshot
from zmena.application.kinds.bridge import BridgeKind


class LightweightLinkBridge(Bridge):
    def __init__(self):
        super().__init__(BridgeKind.LIGHTWEIGHT_LINK)

    def translate(self, link):
        return LightweightLinkSnapshot(left=link.left, right=link.right)
