from dataclasses import dataclass

from zmena.domain.migration_forge.core.release_batch import ReleaseBatch  # noqa: TC001
from zmena.domain.migration_forge.dialects.dialect import Dialect  # noqa: TC001
from zmena.infrastructure.adapters.commands.git import GitCommand  # noqa: TC001


@dataclass
class DeltaCrawlerInboundMessage:
    command: GitCommand
    dialect: Dialect
    release_batch: ReleaseBatch
    commit_from: str
    commit_to: str

    def __repr__(self):
        return (
            f"DeltaCrawlerInboundMessage(commit_from={self.commit_from},commit_to={self.commit_to})"
        )
