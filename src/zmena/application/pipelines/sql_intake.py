from zmena.application.handoffs.sql_intake.messages.outbound import SQLIntakeOutboundMessage
from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.sql_intake.core.sql_table_definition import SQLTableDefinition


class SQLIntakePipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.SQL_INTAKE)
        self.message = message

    def run(self):
        before = SQLTableDefinition(self.message.before)
        after = SQLTableDefinition(self.message.after)

        return SQLIntakeOutboundMessage(
            name=before.name(),
            before=before.columns(),
            after=after.columns(),
        )
