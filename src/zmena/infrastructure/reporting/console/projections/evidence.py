from zmena.infrastructure.reporting.console.views.evidence import EvidenceView


class EvidenceProjection:
    def __repr__(self):
        return "EvidenceProjection(projections=evidence)"

    def apply(self, evidence):
        return EvidenceView(evidence)
