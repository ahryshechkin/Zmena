class Lens:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Lens(kind={self.kind})"
