class SQLColumnProfile:
    def __init__(self, column_def):
        self.column_def = column_def.sql()

    def __repr__(self):
        return f"SQLColumnProfile(definition={self.column_def})"

    def formatted_sql(self):
        name, rest = self.column_def.split(maxsplit=1)
        return f"{name.lower()} {rest.upper()}"
