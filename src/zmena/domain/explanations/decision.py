from src.zmena.domain.explanations.link import LinkExplanation


class DecisionExplanation:
    def __init__(self, links):
        self.link_explanations = [LinkExplanation(link) for link in links]

    def explain(self):
        return self.link_explanations

    def width(self):
        return max(len(link.formatted_header()) for link in self.explain())
