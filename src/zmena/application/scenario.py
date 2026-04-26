from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    sce_id: str
    name: str
    before: list[str]
    after: list[str]
    expected: list[str]

    def __repr__(self):
        return f"Scenario(sce_id={self.sce_id})"
