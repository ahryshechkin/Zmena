from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisResult:
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return "AnalysisResult"
