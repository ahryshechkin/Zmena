from dataclasses import dataclass


@dataclass
class StatementRecord:
    name: str
    attributes: dict

    def __repr__(self):
        return f"StatementRecord(name={self.name},attributes={len(self.attributes)})"
