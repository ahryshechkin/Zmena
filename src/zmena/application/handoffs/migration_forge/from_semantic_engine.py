from zmena.application.handoffs.migration_forge.messages.inbound import MigrationForgeInboundMessage
from zmena.application.handoffs.migration_forge.mints.change import ChangeMint
from zmena.application.handoffs.migration_forge.mints.snapshot import SnapshotMint


class SemanticEngineToMigrationForgeHandoff:
    def __init__(self, seo_message):
        self.seo_message = seo_message

    def __repr__(self):
        return "SemanticEngineToMigrationForgeHandoff(messages=seo)"

    def prepare(self):
        mint = ChangeMint(SnapshotMint())
        snapshots = mint.issue(self.seo_message.decisions)

        return MigrationForgeInboundMessage(matches=snapshots)
