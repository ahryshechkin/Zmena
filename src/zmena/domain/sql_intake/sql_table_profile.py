import sqlglot

from zmena.domain.sql_intake.sql_column_profile import SQLColumnProfile


class SQLTableProfile:
    def __init__(self, ddl):
        self.ddl = ddl

    def __repr__(self):
        return "SQLTableProfile"

    def formatted_columns(self):
        ast = sqlglot.parse_one(self.ddl)

        profiles = [
            SQLColumnProfile(column_def) for column_def in ast.find_all(sqlglot.exp.ColumnDef)
        ]

        return [profile.formatted_sql() for profile in profiles]
