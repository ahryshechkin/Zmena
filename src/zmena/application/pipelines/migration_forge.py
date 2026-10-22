from zmena.application.handoffs.migration_forge.messages.outbound import (
    MigrationForgeOutboundMessage,
)
from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.migration_forge.core.inference import Inference


class MigrationForgePipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.MIGRATION_FORGE)
        self.message = message

    def run(self):
        statements = []
        for change in self.message.changes:
            inference = Inference(change)
            statements.extend(inference.derive())

        return MigrationForgeOutboundMessage(statements=statements)
