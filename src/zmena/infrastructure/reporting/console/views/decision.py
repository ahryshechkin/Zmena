class DecisionView:
    def __init__(self, links):
        self.links = links

    def link_bundle(self):
        return self.links

    def width(self, prefix):
        max_projection_width = max(len(projection.formatted_header()) for projection in self.links)
        return max(max_projection_width, len(prefix) - 2)
