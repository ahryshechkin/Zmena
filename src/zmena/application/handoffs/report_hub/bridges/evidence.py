from zmena.application.handoffs.report_hub.records.evidence import EvidenceRecord


class EvidenceBridge:
    def __repr__(self):
        return "EvidenceBridge(bridges=evidence)"

    def translate(self, evidence):
        return EvidenceRecord(score=evidence.score(), reason=evidence.reason)
