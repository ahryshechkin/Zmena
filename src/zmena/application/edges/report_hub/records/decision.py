from dataclasses import dataclass


@dataclass
class DecisionRecord:
    candidates: list
    winners: list

    def __repr__(self):
        return f"DecisionRecord(candidates={len(self.candidates)},winners={len(self.winners)})"
