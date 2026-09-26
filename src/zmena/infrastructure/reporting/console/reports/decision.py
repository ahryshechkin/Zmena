from zmena.infrastructure.reporting.console.layouts.composite import CompositeReport
from zmena.infrastructure.reporting.console.projections.fragment import FragmentProjection
from zmena.infrastructure.reporting.console.projections.link import LinkProjection
from zmena.infrastructure.reporting.console.reports.evidence import EvidenceReport
from zmena.infrastructure.reporting.console.reports.link import LinkReport
from zmena.infrastructure.reporting.console.views.decision import DecisionView


class DecisionReport(CompositeReport):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        projection = LinkProjection(FragmentProjection())
        for i, decision in enumerate(self.decisions, 1):
            title = self.title(i, candidates=len(decision.candidates))
            report = LinkReport(title, decision.candidates)
            report.render()

            title = self.title(i, candidates=len(decision.candidates))
            report = EvidenceReport(
                title, DecisionView([projection.apply(link) for link in decision.candidates])
            )
            report.render()

            title = self.title(i, winners=len(decision.winners))
            report = LinkReport(title, decision.winners)
            report.render()

            title = self.title(i, winners=len(decision.winners))
            report = EvidenceReport(
                title, DecisionView([projection.apply(link) for link in decision.winners])
            )
            report.render()
