from zmena.infrastructure.reporting.console.views.hypothesis import HypothesisView


class HypothesisMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "HypothesisMint(mints=hypothesis,fragment)"

    def issue(self, hypothesis):
        left, right = hypothesis.key()

        return HypothesisView(
            kind=hypothesis.kind.value,
            left=self.mint.issue(left),
            right=self.mint.issue(right),
        )
