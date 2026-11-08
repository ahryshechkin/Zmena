from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001
from zmena.infrastructure.release_batch import ReleaseBatch  # noqa: TC001


@dataclass
class SQLIntakeInboundMessage:
    label: str
    batch: ReleaseBatch
    dialect: Dialect
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeInboundMessage(label={self.label},name={self.name})"
