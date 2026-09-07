from zmena.domain.migration_forge.kinds.projection import ProjectionKind
from zmena.domain.migration_forge.projections.projection import Projection
from zmena.domain.migration_forge.snapshots.state import StateSnapshot


class StateProjection(Projection):
    def __init__(self):
        super().__init__(ProjectionKind.STATE)

    def from_domain(self, fragment):
        return StateSnapshot(
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.constraint != "NOT NULL",
        )
