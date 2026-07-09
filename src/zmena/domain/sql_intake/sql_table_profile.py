import sqlglot

from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class SQLTableProfile:
    def __init__(self, ddl):
        self.ddl = ddl

    def __repr__(self):
        return "SQLTableProfile"

    def column_profiles(self):
        ast = sqlglot.parse_one(self.ddl)

        profiles = [
            SQLColumnProfile(definition) for definition in ast.find_all(sqlglot.exp.ColumnDef)
        ]

        return [profile.formatted_view() for profile in profiles]
