from zmena.domain.explanations.decision import DecisionExplanation
from zmena.infrastructure.representation.composite.base import ReportComposite
from zmena.infrastructure.representation.custom.explanation import ExplanationReport
from zmena.infrastructure.representation.simple.link import LinkReport


class DecisionReport(ReportComposite):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            candidate_title = self.compose(i, candidates=len(decision.candidates()))
            chosen_title = self.compose(i, chosen=len(decision.chosen()))

            candidate_report = LinkReport(candidate_title, decision.candidates())
            candidate_report.render()

            chosen_report = LinkReport(chosen_title, decision.chosen())
            chosen_report.render()

            explanation_report = ExplanationReport(
                chosen_title, DecisionExplanation(decision.chosen())
            )
            explanation_report.render()
