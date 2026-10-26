class Script:
    def __init__(self, kind, statement):
        self.kind = kind
        self.statement = statement

    def __repr__(self):
        return f"Script(kind={self.kind})"
