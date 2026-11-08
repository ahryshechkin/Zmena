from zmena.application.handoffs.release_vault.messages.inbound import ReleaseVaultInboundMessage
from zmena.application.handoffs.release_vault.mints.migration import MigrationMint
from zmena.infrastructure.project_directory import ProjectDirectory


class SQLIntakeToReleaseVaultHandoff:
    def __init__(self, sio_message, mfo_message):
        self.sio_message = sio_message
        self.mfo_message = mfo_message

    def __repr__(self):
        return "SQLIntakeToReleaseVaultHandoff(messages=sio,mfo)"

    def prepare(self):
        directory = ProjectDirectory()
        release_path = directory.releases() / self.sio_message.release_batch.partition_path()

        mint = MigrationMint()
        migration = "\n".join(mint.issue(script) for script in self.mfo_message.scripts)

        return ReleaseVaultInboundMessage(
            release_path=release_path, tab_name=self.sio_message.tab_name, migration=migration
        )
