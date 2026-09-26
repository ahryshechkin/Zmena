from zmena.infrastructure.reporting.console.views.link import LinkView


class LinkProjection:
    def __init__(self, projection):
        self.projection = projection

    def __repr__(self):
        return "LinkProjection(projections=link,fragment)"

    def apply(self, link):
        return LinkView(
            score=link.score,
            left=self.projection.apply(link.left),
            right=self.projection.apply(link.right),
            evidences=link.evidences,
        )
