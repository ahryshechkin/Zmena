from zmena.infrastructure.representation.basic.fragment import FragmentReport
from zmena.infrastructure.representation.basic.hypothesis import HypothesisReport
from zmena.infrastructure.representation.basic.scenario import ScenarioReport
from zmena.infrastructure.representation.composite.component import ComponentReport
from zmena.infrastructure.representation.composite.decision import DecisionReport


class AnalysisReport:
    def __init__(self, scenario, result):
        self.scenario = scenario
        self.result = result

    def show_scenario(self):
        report = ScenarioReport(self.scenario)
        report.render()

    def show_fragments(self):
        report = FragmentReport("Fragments", self.result.fragments)
        report.render()

    def show_hypotheses(self):
        report = HypothesisReport("Hypotheses", self.result.hypotheses)
        report.render()

    def show_components(self):
        report = ComponentReport(self.result.components)
        report.render()

    def show_decisions(self):
        report = DecisionReport(self.result.decisions)
        report.render()
