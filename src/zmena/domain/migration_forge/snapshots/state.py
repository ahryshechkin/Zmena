from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.snapshot import SnapshotKind
from zmena.domain.migration_forge.snapshots.snapshot import Snapshot


@dataclass
class StateSnapshot(Snapshot):
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return f"State(name={self.name},data_type={self.data_type},nullable={self.nullable})"

    def __post_init__(self):
        super().__init__(SnapshotKind.STATE)
