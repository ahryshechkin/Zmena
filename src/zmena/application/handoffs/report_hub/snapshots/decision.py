from dataclasses import dataclass


@dataclass
class DecisionSnapshot:
    candidates: list
    winners: list

    def __repr__(self):
        return f"DecisionSnapshot(candidates={len(self.candidates)},winners={len(self.winners)})"
