from zmena.domain.semantic_engine.kinds.projection import ProjectionKind
from zmena.domain.semantic_engine.projections.projection import Projection
from zmena.domain.semantic_engine.snapshots.link import LinkSnapshot


class LinkProjection(Projection):
    def __init__(self, projection):
        super().__init__(ProjectionKind.LINK)
        self.projection = projection

    def from_domain(self, link):
        left, right = link.fragments()

        return LinkSnapshot(
            left=self.projection.from_domain(left),
            right=self.projection.from_domain(right),
        )
