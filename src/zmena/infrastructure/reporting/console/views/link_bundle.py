class LinkBundleView:
    def __init__(self, links):
        self.links = links

    def __repr__(self):
        return f"LinkBundleView(links={len(self.links)})"

    def items(self):
        return self.links

    def width(self, prefix):
        header_width = max(len(link.header()) for link in self.links)
        minimum_width = len(prefix) - 2

        return max(header_width, minimum_width)
