from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class ComponentSnapshot(Snapshot):
    fragments: list
    hypotheses: list

    def __repr__(self):
        return (
            f"ComponentSnapshot(fragments={len(self.fragments)},hypotheses={len(self.hypotheses)})"
        )

    def __post_init__(self):
        super().__init__(SnapshotKind.COMPONENT)
