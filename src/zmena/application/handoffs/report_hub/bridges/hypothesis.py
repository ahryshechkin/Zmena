from zmena.application.handoffs.report_hub.bridges.bridge import Bridge
from zmena.application.handoffs.report_hub.snapshots.hypothesis import HypothesisSnapshot
from zmena.application.kinds.bridge import BridgeKind


class HypothesisBridge(Bridge):
    def __init__(self, bridge):
        super().__init__(BridgeKind.LINK)
        self.bridge = bridge

    def translate(self, hypothesis):
        left, right = hypothesis.key()

        return HypothesisSnapshot(
            kind=hypothesis.kind.value,
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
        )
