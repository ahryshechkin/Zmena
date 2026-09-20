from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class DecisionSnapshot(Snapshot):
    candidates: list
    winners: list

    def __repr__(self):
        return f"DecisionSnapshot(candidates={len(self.candidates)},winners={len(self.winners)})"

    def __post_init__(self):
        super().__init__(SnapshotKind.DECISION)
