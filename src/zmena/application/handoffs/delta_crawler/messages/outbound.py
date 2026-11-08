from dataclasses import dataclass

from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001
from zmena.infrastructure.release_batch import ReleaseBatch  # noqa: TC001


@dataclass
class DeltaCrawlerOutboundMessage:
    cmt_id: str
    dialect: Dialect
    release_batch: ReleaseBatch
    name: str
    before: str
    after: str

    def __repr__(self):
        return f"DeltaCrawlerOutboundMessage(cmt_id={self.cmt_id},name={self.name})"
