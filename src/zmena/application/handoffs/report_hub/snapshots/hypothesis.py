from dataclasses import dataclass

from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot  # noqa: TC001


@dataclass
class HypothesisSnapshot:
    kind: str
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __str__(self):
        return f"{self.kind:>18} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"HypothesisSnapshot(kind={self.kind})"
