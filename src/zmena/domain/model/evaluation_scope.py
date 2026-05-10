from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationScope:
    heuristics: list
    links: list

    def __repr__(self):
        return f"EvaluationScope(heuristics={len(self.heuristics)},links={len(self.links)})"
