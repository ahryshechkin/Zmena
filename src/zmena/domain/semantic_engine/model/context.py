from copy import deepcopy


class Context:
    def __init__(self, links):
        self.links = links

    def __repr__(self):
        return f"Context(links={len(self.links)})"

    def original_links(self):
        return self.links

    def cloned_links(self):
        return deepcopy(self.links)
