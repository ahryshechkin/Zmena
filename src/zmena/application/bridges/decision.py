from zmena.domain.semantic_engine.kinds.projection import ProjectionKind
from zmena.domain.semantic_engine.projections.projection import Projection
from zmena.domain.semantic_engine.snapshots.decision import DecisionSnapshot


class DecisionProjection(Projection):
    def __init__(self, projection):
        super().__init__(ProjectionKind.DECISION)
        self.projection = projection

    def from_domain(self, decision):
        selected_links = [self.projection.from_domain(link) for link in decision.winners()]

        return DecisionSnapshot(selected_links=selected_links)
