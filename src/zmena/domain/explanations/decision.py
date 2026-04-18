from src.zmena.domain.explanations.link import ExplanationLink


class ExplanationDecision:
    def __init__(self, links):
        self.explanation_links = [ExplanationLink(link) for link in links]

    def explain(self):
        return self.explanation_links

    def width(self):
        return max(len(link.formatted_header()) for link in self.explain())
