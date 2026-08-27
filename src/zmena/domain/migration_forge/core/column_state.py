from dataclasses import dataclass


@dataclass(frozen=True)
class ColumnState:
    name: str
    data_type: str
    nullable: bool
    position: int

    def __repr__(self):
        return f"ColumnState(name={self.name},position={self.position})"
