from zmena.application.handoffs.test_suite.snapshots.link import LinkSnapshot


class LinkBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "LinkBridge(bridges=fragment,link)"

    def translate(self, link):
        left, right = link.fragments()

        return LinkSnapshot(
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
        )
