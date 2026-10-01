from dataclasses import dataclass

from zmena.application.handoffs.report_hub.records.fragment import FragmentRecord  # noqa: TC001


@dataclass
class HypothesisRecord:
    kind: str
    left: FragmentRecord | None
    right: FragmentRecord | None

    def __repr__(self):
        return f"HypothesisRecord(kind={self.kind})"
