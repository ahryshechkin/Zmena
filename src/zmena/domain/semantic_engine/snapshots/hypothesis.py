from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot  # noqa: TC001
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class HypothesisSnapshot(Snapshot):
    kind: str
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __str__(self):
        return f"{self.kind:>18} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"HypothesisSnapshot(kind={self.kind})"

    def __post_init__(self):
        super().__init__(SnapshotKind.HYPOTHESIS)
