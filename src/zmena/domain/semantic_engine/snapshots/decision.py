from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class DecisionSnapshot(Snapshot):
    selected_links: list

    def __repr__(self):
        return f"DecisionSnapshot(selected_links={len(self.selected_links)}"

    def __post_init__(self):
        super().__init__(SnapshotKind.DECISION)
