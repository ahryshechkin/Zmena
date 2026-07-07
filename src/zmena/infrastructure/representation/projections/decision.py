from zmena.infrastructure.representation.projections.link import LinkProjection


class DecisionProjection:
    def __init__(self, links):
        self.link_projections = [LinkProjection(link) for link in links]

    def links(self):
        return self.link_projections

    def width(self, prefix):
        max_projection_width = max(
            len(projection.formatted_header()) for projection in self.link_projections
        )
        return max(max_projection_width, len(prefix) - 2)
