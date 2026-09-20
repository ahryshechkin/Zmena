from dataclasses import dataclass

from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot  # noqa: TC001
from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class LinkSnapshot(Snapshot):
    score: int
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None
    evidences: list

    def __str__(self):
        return f"{self.score:>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"LinkSnapshot(score={self.score},evidences={len(self.evidences)})"

    def __post_init__(self):
        super().__init__(SnapshotKind.LINK)
