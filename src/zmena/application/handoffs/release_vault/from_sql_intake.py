from zmena.application.handoffs.release_vault.messages.inbound import ReleaseVaultInboundMessage
from zmena.application.handoffs.release_vault.mints.migration import MigrationMint


class SQLIntakeToReleaseVaultHandoff:
    def __init__(self, sio_message, mfo_message):
        self.sio_message = sio_message
        self.mfo_message = mfo_message

    def __repr__(self):
        return "SQLIntakeToReleaseVaultHandoff(messages=sio,mfo)"

    def prepare(self):
        mint = MigrationMint()

        return ReleaseVaultInboundMessage(
            tab_name=self.sio_message.tab_name,
            migration="\n".join(mint.issue(script) for script in self.mfo_message.scripts),
        )
