from dataclasses import dataclass


@dataclass
class FragmentSnapshot:
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
        return f"FragmentSnapshot(tag={self.tag},name={self.name})"
