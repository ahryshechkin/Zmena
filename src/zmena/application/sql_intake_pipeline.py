from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class SQLIntakePipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "SQLIntakePipeline"

    def run(self):
        before = SQLColumnProfile(self.before)
        after = SQLColumnProfile(self.after)

        return before.snapshot(), after.snapshot()
