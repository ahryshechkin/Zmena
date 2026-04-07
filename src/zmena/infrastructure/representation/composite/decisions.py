from zmena.infrastructure.representation.composite.base import ReportComposite
from zmena.infrastructure.representation.custom.explanation import ReportExplanation
from zmena.infrastructure.representation.simple.link import ReportLink


class ReportDecisions(ReportComposite):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            name_candidate = self.compose(i, candidates=len(decision.candidates()))
            report_candidate = ReportLink(decision.candidates(), name_candidate)
            report_candidate.render()

            name_chosen = self.compose(i, links=len(decision.chosen()))
            report_chosen = ReportLink(decision.chosen(), name_chosen)
            report_chosen.render()

            report_explanation = ReportExplanation(decision.explain())
            report_explanation.render()
