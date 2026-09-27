from zmena.application.edges.test_suite.records.link import LinkRecord


class LinkBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "LinkBridge(bridges=link,fragment)"

    def translate(self, link):
        left, right = link.fragments()

        return LinkRecord(
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
        )
