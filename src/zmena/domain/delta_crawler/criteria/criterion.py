class Criterion:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Criterion(kind={self.kind})"

    def apply(self, paths):
        pass
