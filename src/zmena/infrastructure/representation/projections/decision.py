from zmena.infrastructure.representation.projections.link import LinkProjection


class DecisionProjection:
    def __init__(self, links):
        self.link_projections = [LinkProjection(link) for link in links]

    def links(self):
        return self.link_projections

    def width(self):
        return max(len(link.formatted_header()) for link in self.links())
