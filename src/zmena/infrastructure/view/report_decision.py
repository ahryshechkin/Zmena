from zmena.infrastructure.view.report_link import ReportLink


class ReportDecision:
    def __init__(self, decisions):
        self.decisions = decisions

    def render(self):
        self.body()

    def body(self):
        for i, decision in enumerate(self.decisions, 1):
            title = f"\n#### Decision {i}: links={len(decision.chosen())} "

            ReportLink(decision.chosen()).render(title)
