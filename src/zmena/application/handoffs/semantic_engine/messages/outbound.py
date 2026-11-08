from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class SemanticEngineOutboundMessage:
    dialect: Dialect
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
