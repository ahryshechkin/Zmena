from zmena.infrastructure.representation.projections.fragment import FragmentProjection


class LinkProjection:
    def __init__(self, link):
        self.link = link

    def formatted_header(self):
        left, right = self.link.fragments()
        return (
            f"Link: {FragmentProjection(left).caption()} -> {FragmentProjection(right).caption()}"
        )

    def formatted_score(self):
        return f"Score: {self.link.score()}"

    def evidences(self):
        return self.link.justification()
