from dataclasses import dataclass


@dataclass(frozen=True)
class AssessContext:
    heuristics: list
    links: list

    def __repr__(self):
        return f"AssessContext(heuristics={len(self.heuristics)},links={len(self.links)})"
