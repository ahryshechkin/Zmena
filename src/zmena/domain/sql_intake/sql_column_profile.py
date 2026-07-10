class SQLColumnProfile:
    def __init__(self, definition):
        self.definition = definition.sql()

    def __repr__(self):
        return f"SQLColumnProfile(definition={self.definition})"

    def formatted_view(self):
        name, rest = self.definition.split(maxsplit=1)
        return f"{name.lower()} {rest.upper()}"
