from zmena.infrastructure.view.report_composite import ReportComposite
from zmena.infrastructure.view.report_link import ReportLink


class ReportDecision(ReportComposite):
    def __init__(self, decisions):
        self.decisions = decisions

    def body(self):
        for i, decision in enumerate(self.decisions, 1):
            title = f"Decision {i}: links={len(decision.chosen())}"

            report_link = ReportLink(decision.chosen(), title)
            report_link.render()
