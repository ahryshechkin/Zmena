from zmena.infrastructure.representation.layouts.composite import CompositeReport
from zmena.infrastructure.representation.projections.decision import DecisionProjection
from zmena.infrastructure.representation.reports.explanation import ExplanationReport
from zmena.infrastructure.representation.reports.link import LinkReport


class DecisionReport(CompositeReport):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            title = self.title(i, candidates=len(decision.candidates()))
            candidate_report = LinkReport(title, decision.candidates())
            candidate_report.render()

            title = self.title(i, chosen=len(decision.chosen()))
            chosen_report = LinkReport(title, decision.chosen())
            chosen_report.render()

            title = self.title(i, links=len(decision.chosen()))
            explanation_report = ExplanationReport(title, DecisionProjection(decision.chosen()))
            explanation_report.render()
