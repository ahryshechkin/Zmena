from zmena.infrastructure.reporting.console.projections.fragment import FragmentProjection


class LinkProjection:
    def __init__(self, link):
        self.link = link

    def formatted_header(self):
        left = FragmentProjection(self.link.left).caption()
        right = FragmentProjection(self.link.right).caption()
        return f"Link: {left} -> {right}"

    def formatted_score(self):
        return f"Score: {self.link.score}"

    def evidences(self):
        return self.link.evidences
