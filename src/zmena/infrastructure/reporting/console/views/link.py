from zmena.infrastructure.reporting.console.views.fragment import FragmentView


class LinkView:
    def __init__(self, score, left, right, evidences):
        self.score = score
        self.left = left
        self.right = right
        self.evidences = evidences

    def __str__(self):
        return f"{self.score:>7} | #### | {self.left} | #### | {self.right}"

    def formatted_header(self):
        left = FragmentView(self.left).caption()
        right = FragmentView(self.right).caption()
        return f"Link: {left} -> {right}"

    def formatted_score(self):
        return f"Score: {self.score}"

    def evidences(self):
        return self.evidences
