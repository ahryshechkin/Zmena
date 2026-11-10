from dataclasses import dataclass

from zmena.domain.migration_forge.core.release_batch import ReleaseBatch  # noqa: TC001
from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001


@dataclass
class SQLIntakeInboundMessage:
    label: str
    dialect: Dialect
    release_batch: ReleaseBatch
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"SQLIntakeInboundMessage(label={self.label},name={self.name})"
