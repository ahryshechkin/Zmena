class CompositeReport:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Report(composite={self.name})"

    def title(self, idx, **metrics):
        desc = ", ".join(f"{k}={v}" for k, v in metrics.items())
        return f"{self.name} {idx}: {desc}"
