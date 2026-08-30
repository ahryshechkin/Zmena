from dataclasses import dataclass


@dataclass
class Snapshot:
    name: str
    data_type: str
    nullable: bool
    position: int

    def __repr__(self):
        return f"Snapshot(name={self.name},position={self.position})"
