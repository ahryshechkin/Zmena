from dataclasses import dataclass


@dataclass(frozen=True)
class SQLIntakeMessage:
    path: str
    annotation: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeMessage(path={self.path})"
