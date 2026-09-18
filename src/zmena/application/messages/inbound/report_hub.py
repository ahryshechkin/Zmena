from dataclasses import dataclass


@dataclass
class ReportHubInboundMessage:
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
        return f"ReportHubInboundMessage(kind={self.kind},label={self.label})"
