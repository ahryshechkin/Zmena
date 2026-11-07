from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class SQLIntakeInboundMessage:
    label: str
    batch_path: str
    dialect: Dialect
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeInboundMessage(label={self.label},name={self.name})"
