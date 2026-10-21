class SQLColumnDefinition:
    def __init__(self, column_def):
        self.text = column_def.sql()

    def __repr__(self):
        return f"SQLColumnDefinition(text={self.text})"

    def normalized_text(self):
        name, rest = self.text.split(maxsplit=1)
        return f"{name.lower()} {rest.upper()}"
