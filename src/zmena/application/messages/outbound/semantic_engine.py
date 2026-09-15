from dataclasses import dataclass


@dataclass
class SemanticEngineOutboundMessage:
    fragments: list
    hypotheses: list
    components: list
    decisions: list

    def __repr__(self):
        return (
            f"SemanticEngineOutboundMessage("
            f"fragments={len(self.fragments)},hypotheses={len(self.hypotheses)},"
            f"components={len(self.components)},decisions={len(self.decisions)}"
            f")"
        )
