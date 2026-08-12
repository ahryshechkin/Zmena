from dataclasses import dataclass


@dataclass(frozen=True)
class SemanticEngineResult:
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return "SemanticEngineResult"
