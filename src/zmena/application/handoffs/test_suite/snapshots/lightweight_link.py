from dataclasses import dataclass

from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot  # noqa: TC001
from zmena.application.handoffs.test_suite.snapshots.snapshot import Snapshot


@dataclass
class LightweightLinkSnapshot(Snapshot):
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __repr__(self):
        return (
            f"LightweightLinkSnapshot(left={self.left is not None},right={self.right is not None})"
        )
