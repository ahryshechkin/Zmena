from dataclasses import dataclass


@dataclass
class StatementRecord:
    kind: str
    attrs: dict

    def __repr__(self):
        return f"StatementRecord(kind={self.kind},attrs={len(self.attrs)})"
