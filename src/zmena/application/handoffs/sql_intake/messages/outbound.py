from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class SQLIntakeOutboundMessage:
    batch_path: str
    dialect: Dialect
    tab_name: str
    before: list
    after: list

    def __repr__(self):
        return (
            f"SQLIntakeOutboundMessage("
            f"tab_name={self.tab_name},before={len(self.before)},after={len(self.after)}"
            f")"
        )
