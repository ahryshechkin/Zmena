from zmena.infrastructure.reporting.console.views.evidence import EvidenceView


class EvidenceMint:
    def __repr__(self):
        return "EvidenceMint(mints=evidence)"

    def issue(self, evidence):
        return EvidenceView(evidence.score(), evidence.reason)
