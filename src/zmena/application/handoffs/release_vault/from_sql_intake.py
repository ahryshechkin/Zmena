from zmena.application.handoffs.release_vault.messages.inbound import ReleaseVaultInboundMessage
from zmena.application.handoffs.release_vault.mints.migration import MigrationMint
from zmena.infrastructure.project_directory import ProjectDirectory


class SQLIntakeToReleaseVaultHandoff:
    def __init__(self, partition_path, sio_message, mfo_message):
        self.partition_path = partition_path
        self.sio_message = sio_message
        self.mfo_message = mfo_message
        self.directory = ProjectDirectory()

    def __repr__(self):
        return "SQLIntakeToReleaseVaultHandoff(messages=sio,mfo)"

    def prepare(self):
        mint = MigrationMint()

        return ReleaseVaultInboundMessage(
            target_location=self.directory.releases() / self.partition_path,
            tab_name=self.sio_message.tab_name,
            migration="\n".join(mint.issue(script) for script in self.mfo_message.scripts),
        )
