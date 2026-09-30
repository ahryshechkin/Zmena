from zmena.application.edges.test_suite.bridges.statement import StatementBridge
from zmena.application.edges.test_suite.messages.inbound import TestSuiteInboundMessage


class MigrationForgeToTestSuiteHandoff:
    def __init__(self, mfo_message):
        self.mfo_message = mfo_message

    def __repr__(self):
        return "MigrationForgeToTestSuiteHandoff(messages=mfo)"

    def prepare(self):
        bridge = StatementBridge()

        statements = [bridge.translate(statement) for statement in self.mfo_message.statements]

        return TestSuiteInboundMessage(winners=[], statements=statements)
