from dataclasses import dataclass


@dataclass(frozen=True)
class SemanticEngineResult:
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return (
            f"SemanticEngineResult("
            f"fragments={len(self.fragments)},hypotheses={len(self.hypotheses)},"
            f"components={len(self.components)},decisions={len(self.decisions)}"
            f")"
        )
