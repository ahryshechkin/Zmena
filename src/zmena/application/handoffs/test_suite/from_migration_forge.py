from zmena.application.handoffs.test_suite.messages.inbound import TestSuiteInboundMessage
from zmena.application.handoffs.test_suite.mints.statement import StatementMint


class MigrationForgeToTestSuiteHandoff:
    def __init__(self, mfo_message):
        self.mfo_message = mfo_message

    def __repr__(self):
        return "MigrationForgeToTestSuiteHandoff(messages=mfo)"

    def prepare(self):
        mint = StatementMint()

        links = []
        statements = [mint.issue(statement) for statement in self.mfo_message.statements]

        return TestSuiteInboundMessage(links=links, statements=statements)
