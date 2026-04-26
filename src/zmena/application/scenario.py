from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    sce_id: str
    name: str
    before: list
    after: list
    expected: list

    def __repr__(self):
        return f"Scenario(sce_id={self.sce_id})"
