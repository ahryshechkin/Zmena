from zmena.domain.sql_intake.sql_table_profile import SQLTableProfile


class SQLIntakePipeline:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "SQLIntakePipeline"

    def run(self):
        table_profile_before = SQLTableProfile(self.before)
        table_profile_after = SQLTableProfile(self.after)

        return table_profile_before.formatted_columns(), table_profile_after.formatted_columns()
