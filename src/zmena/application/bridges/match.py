from zmena.application.bridges.projection import Projection
from zmena.application.kinds.bridge import ProjectionKind
from zmena.domain.migration_forge.snapshots.match import MatchSnapshot


class MatchProjection(Projection):
    def __init__(self, projection):
        super().__init__(ProjectionKind.MATCH)
        self.projection = projection

    def from_infra(self, decision):
        matches = []
        for selected_link in decision.selected_links:
            match = MatchSnapshot(
                before=self.projection.from_infra(selected_link.left),
                after=self.projection.from_infra(selected_link.right),
            )
            matches.append(match)

        return matches
