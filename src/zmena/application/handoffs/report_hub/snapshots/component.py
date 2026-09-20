from dataclasses import dataclass


@dataclass
class ComponentSnapshot:
    fragments: list
    hypotheses: list

    def __repr__(self):
        return (
            f"ComponentSnapshot(fragments={len(self.fragments)},hypotheses={len(self.hypotheses)})"
        )
