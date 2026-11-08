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
        mint = MigrationMint()

        return ReleaseVaultInboundMessage(
            release_path=directory.releases() / self.sio_message.batch.partition_path(),
            tab_name=self.sio_message.tab_name,
            migration="\n".join(mint.issue(script) for script in self.mfo_message.scripts),
        )
