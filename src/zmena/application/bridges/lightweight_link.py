from zmena.application.bridges.bridge import Bridge
from zmena.application.kinds.bridge import BridgeKind
from zmena.domain.semantic_engine.snapshots.lightweight_link import LightweightLinkSnapshot


class LightweightLinkBridge(Bridge):
    def __init__(self):
        super().__init__(BridgeKind.LIGHTWEIGHT_LINK)

    def translate(self, link):
        return LightweightLinkSnapshot(
            left=link.left,
            right=link.right,
        )
