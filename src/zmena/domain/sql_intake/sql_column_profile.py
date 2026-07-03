import sqlglot


class SQLColumnProfile:
    def __init__(self, ddl):
        self.ddl = ddl

    def snapshot(self):
        ast = sqlglot.parse_one(self.ddl)
        return [col.sql().lower() for col in ast.find_all(sqlglot.exp.ColumnDef)]
