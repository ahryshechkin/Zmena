from zmena.infrastructure.representation.composite.components import ReportComponents
from zmena.infrastructure.representation.composite.decisions import ReportDecisions
from zmena.infrastructure.representation.simple.brick import ReportBrick
from zmena.infrastructure.representation.simple.hypothesis import ReportHypothesis
from zmena.infrastructure.representation.simple.scenario import ReportScenario


class Report:
    def __init__(self, scenario):
        self.scenario = scenario

    def show_scenario(self):
        report = ReportScenario(self.scenario)
        report.render()

    def show_bricks(self, bricks):
        report = ReportBrick(bricks)
        report.render()

    def show_hypotheses(self, hypotheses):
        report = ReportHypothesis(hypotheses)
        report.render()

    def show_components(self, components):
        report = ReportComponents(components)
        report.render()

    def show_decisions(self, decisions):
        report = ReportDecisions(decisions)
        report.render()
