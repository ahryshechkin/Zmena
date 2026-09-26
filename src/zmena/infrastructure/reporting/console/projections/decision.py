from zmena.infrastructure.reporting.console.views.decision import DecisionView


class DecisionProjection:
    def __init__(self, projection):
        self.projection = projection

    def __repr__(self):
        return "DecisionProjection(projections=decision,link,fragment)"

    def apply(self, links):
        return DecisionView([self.projection.apply(link) for link in links])
