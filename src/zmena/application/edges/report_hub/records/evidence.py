from dataclasses import dataclass


@dataclass
class EvidenceRecord:
    score: int
    reason: str

    def __repr__(self):
        return f"EvidenceRecord(score={self.score},reason={self.reason})"
