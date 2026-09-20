from dataclasses import dataclass

from zmena.application.handoffs.test_suite.snapshots.fragment import FragmentSnapshot  # noqa: TC001


@dataclass
class LinkSnapshot:
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __repr__(self):
        return f"LinkSnapshot(left={self.left is not None},right={self.right is not None})"
