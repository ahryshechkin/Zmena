from dataclasses import dataclass


@dataclass(frozen=True)
class SQLIntakeMessage:
    label: str
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeMessage(label={self.label})"
