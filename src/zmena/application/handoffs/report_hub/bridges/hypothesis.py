from zmena.application.handoffs.report_hub.records.hypothesis import HypothesisRecord


class HypothesisBridge:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "HypothesisBridge(mints=hypothesis,fragment)"

    def translate(self, hypothesis):
        left, right = hypothesis.key()

        return HypothesisRecord(
            kind=hypothesis.kind.value,
            left=self.mint.issue(left),
            right=self.mint.issue(right),
        )
