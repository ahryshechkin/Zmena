from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot  # noqa: TC001
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class LightweightLinkSnapshot(Snapshot):
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __repr__(self):
        return (
            f"LightweightLinkSnapshot(left={self.left is not None},right={self.right is not None})"
        )

    def __post_init__(self):
        super().__init__(SnapshotKind.LIGHTWEIGHT_LINK)
