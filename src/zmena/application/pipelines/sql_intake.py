from zmena.application.messages.semantic_engine import SemanticEngineMessage
from zmena.domain.sql_intake.sql_table_profile import SQLTableProfile


class SQLIntakePipeline:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"SQLIntakePipeline(path={self.message.path})"

    def run(self):
        table_profile_before = SQLTableProfile(self.message.before)
        table_profile_after = SQLTableProfile(self.message.after)

        return SemanticEngineMessage(
            before=table_profile_before.formatted_columns(),
            after=table_profile_after.formatted_columns(),
        )
