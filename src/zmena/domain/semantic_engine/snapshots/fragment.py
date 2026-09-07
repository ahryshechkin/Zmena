from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class FragmentSnapshot(Snapshot):
    tag: str
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return (
            f"FragmentSnapshot("
            f"tag={self.tag},name={self.name},data_type={self.data_type},nullable={self.nullable}"
            f")"
        )

    def __post_init__(self):
        super().__init__(SnapshotKind.FRAGMENT)
