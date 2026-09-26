from dataclasses import dataclass


@dataclass
class ComponentRecord:
    fragments: list
    hypotheses: list

    def __repr__(self):
        return f"ComponentRecord(fragments={len(self.fragments)},hypotheses={len(self.hypotheses)})"
