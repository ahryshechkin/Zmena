from zmena.infrastructure.reporting.console.views.link import LinkView


class LinkProjection:
    def __init__(self, fragment_projection, evidence_projection):
        self.fragment_projection = fragment_projection
        self.evidence_projection = evidence_projection

    def __repr__(self):
        return "LinkProjection(projections=link,fragment,evidence)"

    def apply(self, link):
        evidences = [self.evidence_projection.apply(evidence) for evidence in link.evidences]
        return LinkView(
            link.score,
            self.fragment_projection.apply(link.left),
            self.fragment_projection.apply(link.right),
            evidences,
        )
