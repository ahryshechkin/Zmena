from zmena.application.kinds.pipeline import PipelineKind
from zmena.application.messages.outbound.sql_intake import SQLIntakeOutboundMessage
from zmena.application.pipelines.pipeline import Pipeline
from zmena.domain.sql_intake.core.sql_table_profile import SQLTableProfile


class SQLIntakePipeline(Pipeline):
    def __init__(self, message):
        super().__init__(PipelineKind.SQL_INTAKE)
        self.message = message

    def run(self):
        table_profile_before = SQLTableProfile(self.message.before)
        table_profile_after = SQLTableProfile(self.message.after)

        return SQLIntakeOutboundMessage(
            before=table_profile_before.formatted_columns(),
            after=table_profile_after.formatted_columns(),
        )
