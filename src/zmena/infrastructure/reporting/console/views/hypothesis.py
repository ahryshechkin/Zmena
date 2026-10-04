class HypothesisView:
    def __init__(self, kind, left, right):
        self.kind = kind
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.kind:>18} | #### | {self.left} | #### | {self.right}"

    def __repr__(self):
        return f"HypothesisView(kind={self.kind})"
