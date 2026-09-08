from zmena.application.bridges.projection import Projection
from zmena.application.kinds.bridge import ProjectionKind
from zmena.domain.migration_forge.snapshots.state import StateSnapshot


class StateProjection(Projection):
    def __init__(self):
        super().__init__(ProjectionKind.STATE)

    def from_infra(self, fragment):
        if fragment.tag == "stub":
            return None

        return StateSnapshot(
            name=fragment.name,
            data_type=fragment.data_type,
            nullable=fragment.nullable,
        )
