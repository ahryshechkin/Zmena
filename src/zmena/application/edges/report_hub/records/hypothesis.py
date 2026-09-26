from dataclasses import dataclass

from zmena.application.edges.report_hub.records.fragment import FragmentSnapshot  # noqa: TC001


@dataclass
class HypothesisSnapshot:
    kind: str
    left: FragmentSnapshot | None
    right: FragmentSnapshot | None

    def __repr__(self):
        return f"HypothesisSnapshot(kind={self.kind})"
