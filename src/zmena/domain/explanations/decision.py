class ExplanationDecision:
    def __init__(self, links):
        self.links = links

    def length(self):
        return max(len(link.summary()) for link in self.links)
