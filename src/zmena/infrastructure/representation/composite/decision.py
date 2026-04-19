from zmena.domain.explanations.decision import DecisionExplanation
from zmena.infrastructure.representation.basic.link import LinkReport
from zmena.infrastructure.representation.composite.base import CompositeReport
from zmena.infrastructure.representation.specialized.explanation import ExplanationReport


class DecisionReport(CompositeReport):
    def __init__(self, decisions):
        super().__init__("Decision")
        self.decisions = decisions

    def render(self):
        for i, decision in enumerate(self.decisions, 1):
            candidate_title = self.title(i, candidates=len(decision.candidates()))
            chosen_title = self.title(i, chosen=len(decision.chosen()))

            candidate_report = LinkReport(candidate_title, decision.candidates())
            candidate_report.render()

            chosen_report = LinkReport(chosen_title, decision.chosen())
            chosen_report.render()

            explanation_report = ExplanationReport(
                chosen_title, DecisionExplanation(decision.chosen())
            )
            explanation_report.render()
