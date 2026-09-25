from zmena.infrastructure.reporting.console.bridges.fragment import FragmentBridge
from zmena.infrastructure.reporting.console.bridges.hypothesis import HypothesisBridge
from zmena.infrastructure.reporting.console.bridges.statement import StatementBridge
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
        bridge = FragmentBridge()
        fragments = [bridge.translate(fragment) for fragment in self.message.fragments]
        report = FragmentReport("Fragments", fragments)
        report.render()

    def show_hypotheses(self):
        bridge = HypothesisBridge(FragmentBridge())
        hypotheses = [bridge.translate(hypothesis) for hypothesis in self.message.hypotheses]
        report = HypothesisReport("Hypotheses", hypotheses)
        report.render()

    def show_components(self):
        report = ComponentReport(self.message.components)
        report.render()

    def show_decisions(self):
        report = DecisionReport(self.message.decisions)
        report.render()

    def show_statements(self):
        bridge = StatementBridge()
        statements = [bridge.translate(statement) for statement in self.message.statements]
        report = StatementReport("Statements", statements)
        report.render()
