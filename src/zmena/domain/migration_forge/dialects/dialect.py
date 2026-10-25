class Dialect:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Dialect(kind={self.kind})"
