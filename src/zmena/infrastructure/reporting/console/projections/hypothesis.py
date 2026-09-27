from zmena.infrastructure.reporting.console.views.hypothesis import HypothesisView


class HypothesisProjection:
    def __init__(self, projection):
        self.projection = projection

    def __repr__(self):
        return "HypothesisProjection(projections=hypothesis,fragment)"

    def apply(self, hypothesis):
        return HypothesisView(
            hypothesis.kind,
            self.projection.apply(hypothesis.left),
            self.projection.apply(hypothesis.right),
        )
