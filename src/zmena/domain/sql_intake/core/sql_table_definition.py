import sqlglot

from zmena.domain.sql_intake.core.sql_column_definition import SQLColumnDefinition


class SQLTableDefinition:
    def __init__(self, ddl):
        self.ddl = ddl

    def __repr__(self):
        return f"SQLTableDefinition(length={len(self.ddl)})"

    def normalized_columns(self):
        ast = sqlglot.parse_one(self.ddl)

        definitions = [
            SQLColumnDefinition(column_def) for column_def in ast.find_all(sqlglot.exp.ColumnDef)
        ]

        return [definition.normalized_text() for definition in definitions]
