from zmena.domain.explanations.decision import DecisionExplanation
from zmena.infrastructure.representation.basic.link import LinkReport
from zmena.infrastructure.representation.composite.composite_report import CompositeReport
from zmena.infrastructure.representation.specialized.explanation import ExplanationReport


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
            explanation_report = ExplanationReport(title, DecisionExplanation(decision.chosen()))
            explanation_report.render()
