from dataclasses import dataclass

from zmena.application.handoffs.report_hub.records.fragment import FragmentRecord  # noqa: TC001


@dataclass
class LinkRecord:
    score: int
    left: FragmentRecord | None
    right: FragmentRecord | None
    evidences: list

    def __repr__(self):
        return f"LinkRecord(score={self.score},evidences={len(self.evidences)})"
