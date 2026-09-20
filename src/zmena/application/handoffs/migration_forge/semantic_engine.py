from zmena.application.handoffs.migration_forge.bridges.match_bundle import MatchBundleBridge
from zmena.application.handoffs.migration_forge.bridges.state import StateBridge
from zmena.application.messages.inbound.migration_forge import MigrationForgeInboundMessage


class SemanticEngineToMigrationForgeHandoff:
    def __init__(self, seo_message):
        self.seo_message = seo_message

    def __repr__(self):
        return "SemanticEngineToMigrationForgeHandoff(messages=seo)"

    def prepare(self):
        bridge = MatchBundleBridge(StateBridge())
        matches = bridge.translate(self.seo_message.decisions)

        return MigrationForgeInboundMessage(matches=matches)
