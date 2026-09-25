from zmena.infrastructure.reporting.console.views.hypothesis import HypothesisView


class HypothesisBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "HypothesisBridge(bridges=fragment,hypothesis)"

    def translate(self, hypothesis):
        return HypothesisView(
            kind=hypothesis.kind,
            left=self.bridge.translate(hypothesis.left),
            right=self.bridge.translate(hypothesis.right),
        )
