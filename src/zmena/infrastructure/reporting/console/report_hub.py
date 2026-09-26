from zmena.infrastructure.reporting.console.projections.statement import StatementProjection
from zmena.infrastructure.reporting.console.reports.component import ComponentReport
from zmena.infrastructure.reporting.console.reports.decision import DecisionReport
from zmena.infrastructure.reporting.console.reports.fragment import FragmentReport
from zmena.infrastructure.reporting.console.reports.hypothesis import HypothesisReport
from zmena.infrastructure.reporting.console.reports.sql_diff import SQLDiffReport
from zmena.infrastructure.reporting.console.reports.statement import StatementReport


class ReportHub:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"ReportHub(sce_id={self.message.label},name={self.message.name})"

    def show_sql_diff(self):
        report = SQLDiffReport(self.message)
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

    def show_statements(self):
        projection = StatementProjection()
        statements = [projection.apply(statement) for statement in self.message.statements]
        report = StatementReport("Statements", statements)
        report.render()
