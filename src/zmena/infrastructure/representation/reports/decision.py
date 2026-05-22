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
            report = LinkReport(title, decision.candidates())
            report.render()

            title = self.title(i, winners=len(decision.winners()))
            report = LinkReport(title, decision.winners())
            report.render()

            title = self.title(i, candidates=len(decision.candidates()))
            report = EvidenceReport(title, DecisionProjection(decision.candidates()))
            report.render()

            title = self.title(i, winners=len(decision.winners()))
            report = EvidenceReport(title, DecisionProjection(decision.winners()))
            report.render()
