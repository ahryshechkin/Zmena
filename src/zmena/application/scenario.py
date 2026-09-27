from dataclasses import dataclass


@dataclass
class Scenario:
    sce_id: str
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"Scenario(sce_id={self.sce_id})"
