from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class MigrationForgeInboundMessage:
    dialect: Dialect
    changes: list

    def __repr__(self):
        return f"MigrationForgeInboundMessage(changes={len(self.changes)})"
