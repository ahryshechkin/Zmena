from zmena.infrastructure.representation.composite.base import ReportComposite
from zmena.infrastructure.representation.simple.link import ReportLink


class ReportDecision(ReportComposite):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            name = self.compose(i, links=len(decision.chosen()))

            report_link = ReportLink(decision.chosen(), name)
            report_link.render()
