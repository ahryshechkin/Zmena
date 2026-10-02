from zmena.infrastructure.reporting.console.layouts.composite import CompositeReport
from zmena.infrastructure.reporting.console.reports.evidence import EvidenceReport
from zmena.infrastructure.reporting.console.reports.link import LinkReport
from zmena.infrastructure.reporting.console.views.link_bundle import LinkBundleView


class DecisionReport(CompositeReport):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            title = self.title(i, candidates=len(decision.candidates()))
            report = LinkReport(title, decision.candidates())
            report.render()
            report = EvidenceReport(title, LinkBundleView(decision.candidates()))
            report.render()

            title = self.title(i, winners=len(decision.winners()))
            report = LinkReport(title, decision.winners())
            report.render()
            report = EvidenceReport(title, LinkBundleView(decision.winners()))
            report.render()
