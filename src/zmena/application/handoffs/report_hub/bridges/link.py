from zmena.application.handoffs.report_hub.snapshots.link import LinkSnapshot


class LinkBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def translate(self, link):
        left, right = link.fragments()

        return LinkSnapshot(
            score=link.score(),
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
            evidences=link.evidences,
        )
