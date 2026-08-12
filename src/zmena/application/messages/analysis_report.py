from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisReportMessage:
    sce_id: str
    name: str
    before: list
    after: list
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return "AnalysisReportMessage"
