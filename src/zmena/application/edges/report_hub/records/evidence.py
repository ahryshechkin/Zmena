from dataclasses import dataclass


@dataclass
class EvidenceRecord:
    score: int

    def __repr__(self):
        return f"EvidenceRecord(score={self.score})"
