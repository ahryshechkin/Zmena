from zmena.infrastructure.representation.basic.fragment import FragmentReport
from zmena.infrastructure.representation.basic.hypothesis import HypothesisReport
from zmena.infrastructure.representation.basic.scenario import ScenarioReport
from zmena.infrastructure.representation.composite.component import ComponentReport
from zmena.infrastructure.representation.composite.decision import DecisionReport


class Report:
    def __init__(self, scenario):
        self.scenario = scenario

    def show_scenario(self):
        report = ScenarioReport(self.scenario)
        report.render()

    def show_fragments(self, fragments):
        report = FragmentReport("Fragments", fragments)
        report.render()

    def show_hypotheses(self, hypotheses):
        report = HypothesisReport("Hypotheses", hypotheses)
        report.render()

    def show_components(self, components):
        report = ComponentReport(components)
        report.render()

    def show_decisions(self, decisions):
        report = DecisionReport(decisions)
        report.render()
