from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class SemanticEngineInboundMessage:
    dialect: Dialect
    before: str
    after: str

    def __repr__(self):
        return f"SemanticEngineInboundMessage(before={len(self.before)},after={len(self.after)})"
