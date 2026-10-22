from zmena.application.handoffs.migration_forge.messages.inbound import MigrationForgeInboundMessage
from zmena.application.handoffs.migration_forge.mints.change import ChangeMint
from zmena.application.handoffs.migration_forge.mints.snapshot import SnapshotMint


class SQLIntakeToMigrationForgeHandoff:
    def __init__(self, sio_message, seo_message):
        self.sio_message = sio_message
        self.seo_message = seo_message

    def __repr__(self):
        return "SQLIntakeToMigrationForgeHandoff(messages=sio,seo)"

    def prepare(self):
        mint = ChangeMint(SnapshotMint())
        changes = mint.issue(self.sio_message.tab_name, self.seo_message.decisions)

        return MigrationForgeInboundMessage(changes=changes)
