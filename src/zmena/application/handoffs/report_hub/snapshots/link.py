from dataclasses import dataclass

from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot  # noqa: TC001


@dataclass
class LinkSnapshot:
    score: int
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None
    evidences: list

    def __str__(self):
        return f"{self.score:>7} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"LinkSnapshot(score={self.score},evidences={len(self.evidences)})"
