from zmena.domain.sql_intake.sql_table_profile import SQLTableProfile


class SQLIntakePipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "SQLIntakePipeline"

    def run(self):
        before = SQLTableProfile(self.before)
        after = SQLTableProfile(self.after)

        return before.snapshot(), after.snapshot()
