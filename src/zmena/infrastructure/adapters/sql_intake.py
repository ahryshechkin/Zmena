import sqlglot


class SQLIntake:
    def __init__(self, ddl):
        self.ddl = ddl

    def columns(self):
        ast = sqlglot.parse_one(self.ddl)
        return [col.sql() for col in ast.find_all(sqlglot.exp.ColumnDef)]
