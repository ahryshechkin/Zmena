class ComponentView:
    def __init__(self, fragments, hypotheses):
        self.fragments = fragments
        self.hypotheses = hypotheses

    def __repr__(self):
        return f"ComponentView(fragments={len(self.fragments)},hypotheses={len(self.hypotheses)})"
