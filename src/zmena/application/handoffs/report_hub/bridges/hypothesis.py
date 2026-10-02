from zmena.infrastructure.reporting.console.views.hypothesis import HypothesisView


class HypothesisMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "HypothesisMint(mints=hypothesis,fragment)"

    def issue(self, hypothesis):
        left, right = hypothesis.key()

        return HypothesisView(hypothesis.kind.value, self.mint.issue(left), self.mint.issue(right))
