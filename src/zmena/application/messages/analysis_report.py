from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisReportMessage:
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
        return f"AnalysisReportMessage(sce_id={self.entity_id})"
