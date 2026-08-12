from zmena.infrastructure.representation.reports.component import ComponentReport
from zmena.infrastructure.representation.reports.decision import DecisionReport
from zmena.infrastructure.representation.reports.fragment import FragmentReport
from zmena.infrastructure.representation.reports.hypothesis import HypothesisReport
from zmena.infrastructure.representation.reports.scenario import ScenarioReport


class AnalysisReport:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"AnalysisReport(sce_id={self.message.sce_id},name={self.message.name})"

    def show_scenario(self):
        report = ScenarioReport(self.message)
        report.render()

    def show_fragments(self):
        report = FragmentReport("Fragments", self.message.fragments)
        report.render()

    def show_hypotheses(self):
        report = HypothesisReport("Hypotheses", self.message.hypotheses)
        report.render()

    def show_components(self):
        report = ComponentReport(self.message.components)
        report.render()

    def show_decisions(self):
        report = DecisionReport(self.message.decisions)
        report.render()
