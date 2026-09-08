from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.snapshot import SnapshotKind
from zmena.domain.migration_forge.snapshots.snapshot import Snapshot
from zmena.domain.migration_forge.snapshots.state import StateSnapshot  # noqa: TC001


@dataclass
class MatchSnapshot(Snapshot):
    before: StateSnapshot | None
    after: StateSnapshot | None

    def __repr__(self):
        return f"MatchSnapshot(before={self.before is not None},after={self.after is not None})"

    def __post_init__(self):
        super().__init__(SnapshotKind.MATCH)
