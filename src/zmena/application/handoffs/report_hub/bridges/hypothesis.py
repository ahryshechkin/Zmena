from zmena.application.handoffs.report_hub.snapshots.hypothesis import HypothesisSnapshot


class HypothesisBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "HypothesisBridge(bridges=fragment,hypothesis)"

    def translate(self, hypothesis):
        left, right = hypothesis.key()

        return HypothesisSnapshot(
            kind=hypothesis.kind.value,
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
        )
