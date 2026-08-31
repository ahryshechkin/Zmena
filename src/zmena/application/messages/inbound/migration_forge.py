from dataclasses import dataclass

from zmena.domain.migration_forge.core.snapshot import Snapshot  # noqa: TC001


@dataclass
class MigrationForgeInboundMessage:
    before: Snapshot
    after: Snapshot

    def __repr__(self):
        return (
            f"MigrationForgeMessage("
            f"before={self.before is not None},after={self.after is not None}"
            f")"
        )
