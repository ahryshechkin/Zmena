from zmena.application.messages.outbound.migration_forge import MigrationForgeOutboundMessage
from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan


class MigrationForgePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "MigrationForgePipeline"

    def run(self):
        statements = []
        for match in self.message.matches:
            change = Change(match.before, match.after)
            plan = Plan(change)
            statements.extend(plan.derive())

        return MigrationForgeOutboundMessage(statements=statements)
