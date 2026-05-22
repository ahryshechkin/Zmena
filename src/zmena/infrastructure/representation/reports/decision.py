from zmena.infrastructure.representation.layouts.composite import CompositeReport
from zmena.infrastructure.representation.projections.decision import DecisionProjection
from zmena.infrastructure.representation.reports.evidence import EvidenceReport
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

            title = self.title(i, winners=len(decision.winners()))
            winner_report = LinkReport(title, decision.winners())
            winner_report.render()

            title = self.title(i, candidates=len(decision.candidates()))
            explanation_report = EvidenceReport(title, DecisionProjection(decision.candidates()))
            explanation_report.render()

            title = self.title(i, winners=len(decision.winners()))
            explanation_report = EvidenceReport(title, DecisionProjection(decision.winners()))
            explanation_report.render()
