from zmena.infrastructure.reporting.console.views.link import LinkView


class LinkProjection:
    def __init__(self, projection):
        self.projection = projection

    def __repr__(self):
        return "LinkProjection(projections=link,fragment)"

    def apply(self, link):
        return LinkView(
            link.score,
            self.projection.apply(link.left),
            self.projection.apply(link.right),
            link.evidences,
        )
