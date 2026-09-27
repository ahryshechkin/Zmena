from zmena.application.edges.report_hub.records.evidence import EvidenceRecord


class EvidenceBridge:
    def __repr__(self):
        return "EvidenceBridge(bridges=evidence)"

    def translate(self, evidence):
        return EvidenceRecord(score=evidence.score())
