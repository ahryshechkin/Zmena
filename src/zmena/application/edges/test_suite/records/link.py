from dataclasses import dataclass

from zmena.application.edges.test_suite.records.fragment import FragmentSnapshot  # noqa: TC001


@dataclass
class LinkSnapshot:
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __repr__(self):
        return f"LinkSnapshot(left={self.left is not None},right={self.right is not None})"
