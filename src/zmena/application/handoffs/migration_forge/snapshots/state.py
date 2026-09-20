from dataclasses import dataclass

from zmena.application.handoffs.migration_forge.snapshots.snapshot import Snapshot
from zmena.domain.migration_forge.kinds.snapshot import SnapshotKind


@dataclass
class StateSnapshot(Snapshot):
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return (
            f"StateSnapshot(name={self.name},data_type={self.data_type},nullable={self.nullable})"
        )

    def __post_init__(self):
        super().__init__(SnapshotKind.STATE)
