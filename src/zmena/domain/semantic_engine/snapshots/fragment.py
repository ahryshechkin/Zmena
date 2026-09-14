from dataclasses import dataclass

from zmena.domain.semantic_engine.kinds.snapshot import SnapshotKind
from zmena.domain.semantic_engine.snapshots.snapshot import Snapshot


@dataclass
class FragmentSnapshot(Snapshot):
    tag: str
    block: str
    position: str
    side: str
    name: str
    data_type: str
    nullable: bool

    def __str__(self):
        nullable = "" if self.nullable else "NOT NULL"
        return (
            f"{self.tag:>8} | {self.block:>8} | "
            f"{self.position:>8} | {self.side:>4} | "
            f"{self.name:<7} | {self.data_type:<13} | {nullable:>10}"
        )

    def __repr__(self):
        return (
            f"FragmentSnapshot("
            f"tag={self.tag},name={self.name},data_type={self.data_type},nullable={self.nullable}"
            f")"
        )

    def __post_init__(self):
        super().__init__(SnapshotKind.FRAGMENT)
