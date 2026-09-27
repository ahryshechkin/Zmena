from zmena.application.edges.report_hub.records.link import LinkRecord


class LinkBridge:
    def __init__(self, bridge):
        self.bridge = bridge

    def __repr__(self):
        return "LinkBridge(bridges=link,evidences,fragment)"

    def translate(self, link):
        left, right = link.fragments()

        return LinkRecord(
            score=link.score(),
            left=self.bridge.translate(left),
            right=self.bridge.translate(right),
            evidences=link.evidences,
        )
