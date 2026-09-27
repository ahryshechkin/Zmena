from zmena.infrastructure.reporting.console.views.link import LinkView


class LinkProjection:
    def __init__(self, fragment_projection, evidence_projection):
        self.fragment_projection = fragment_projection
        self.evidence_projection = evidence_projection

    def __repr__(self):
        return "LinkProjection(projections=link,evidence,fragment)"

    def apply(self, link):
        return LinkView(
            link.score,
            self.fragment_projection.apply(link.left),
            self.fragment_projection.apply(link.right),
            [self.evidence_projection.apply(evidence) for evidence in link.evidences],
        )
