from zmena.application.handoffs.test_suite.bridges.fragment import FragmentBridge
from zmena.application.handoffs.test_suite.bridges.link import LinkBridge
from zmena.application.handoffs.test_suite.messages.inbound import TestSuiteInboundMessage


class SemanticEngineToTestSuiteHandoff:
    def __init__(self, seo_message):
        self.seo_message = seo_message

    def __repr__(self):
        return "SemanticEngineToTestSuiteHandoff(messages=seo)"

    def prepare(self):
        bridge = LinkBridge(FragmentBridge())

        winners = []
        for decision in self.seo_message.decisions:
            winners.extend(decision.winners())

        links = [bridge.translate(winner) for winner in winners]
        statements = []

        return TestSuiteInboundMessage(links=links, statements=statements)
