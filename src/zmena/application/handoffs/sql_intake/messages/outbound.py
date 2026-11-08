from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001
from zmena.infrastructure.release_batch import ReleaseBatch  # noqa: TC001


@dataclass
class SQLIntakeOutboundMessage:
    dialect: Dialect
    release_batch: ReleaseBatch
    tab_name: str
    before: list
    after: list

    def __repr__(self):
        return (
            f"SQLIntakeOutboundMessage("
            f"tab_name={self.tab_name},before={len(self.before)},after={len(self.after)}"
            f")"
        )
