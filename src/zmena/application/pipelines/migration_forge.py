from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.messages.outbound.migration_forge import MigrationForgeOutboundMessage
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.migration_forge.core.change import Change
from zmena.domain.migration_forge.core.plan import Plan


class MigrationForgePipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.MIGRATION_FORGE)
        self.message = message

    def run(self):
        statements = []
        for match in self.message.matches:
            change = Change(match.before, match.after)
            plan = Plan(change)
            statements.extend(plan.derive())

        return MigrationForgeOutboundMessage(statements=statements)
