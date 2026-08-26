from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ColumnState:
    name: str
    position: int
    data_type: str
    nullable: bool

    def __repr__(self):
        return f"ColumnState(name={self.name},position={self.position})"
