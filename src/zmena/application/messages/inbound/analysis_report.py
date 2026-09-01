from dataclasses import dataclass


@dataclass
class AnalysisReportInboundMessage:
    kind: str
    label: str
    name: str
    before: list
    after: list
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return f"AnalysisReportInboundMessage(kind={self.kind},label={self.label})"
