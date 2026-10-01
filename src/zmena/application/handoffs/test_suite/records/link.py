from dataclasses import dataclass

from zmena.application.handoffs.test_suite.records.fragment import FragmentRecord  # noqa: TC001


@dataclass
class LinkRecord:
    left: FragmentRecord | None
    right: FragmentRecord | None

    def __repr__(self):
        return f"LinkRecord(left={self.left is not None},right={self.right is not None})"
