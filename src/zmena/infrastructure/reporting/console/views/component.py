class ComponentView:
    def __init__(self, fragment_bundle, hypothesis_bundle):
        self.fragment_bundle = fragment_bundle
        self.hypothesis_bundle = hypothesis_bundle

    def __repr__(self):
        return (
            f"ComponentView(fragments={len(self.fragments())},hypotheses={len(self.hypotheses())})"
        )

    def fragments(self):
        return self.fragment_bundle

    def hypotheses(self):
        return self.hypothesis_bundle
