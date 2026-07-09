import sqlglot


class SQLTableProfile:
    def __init__(self, ddl):
        self.ddl = ddl

    def __repr__(self):
        return "SQLTableProfile"

    def snapshot(self):
        ast = sqlglot.parse_one(self.ddl)

        for col in ast.find_all(sqlglot.exp.ColumnDef):
            print(col.sql())
        return [col.sql().upper() for col in ast.find_all(sqlglot.exp.ColumnDef)]
