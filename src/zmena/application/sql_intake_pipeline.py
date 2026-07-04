from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class SQLIntakePipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "SQLIntakePipeline"

    def run(self):
        sql_column_profile_before = SQLColumnProfile(self.before)
        sql_column_profile_after = SQLColumnProfile(self.after)

        return sql_column_profile_before.snapshot(), sql_column_profile_after.snapshot()
