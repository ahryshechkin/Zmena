from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.snapshot import SnapshotKind
from zmena.domain.migration_forge.snapshots.snapshot import Snapshot


@dataclass
class MatchSnapshot(Snapshot):
    before_tag: str
    before_name: str
    before_data_type: str
    before_nullability: bool
    after_tag: str
    after_name: str
    after_data_type: str
    after_nullability: bool

    def __repr__(self):
        return "MatchSnapshot"

    def __post_init__(self):
        super().__init__(SnapshotKind.MATCH)
