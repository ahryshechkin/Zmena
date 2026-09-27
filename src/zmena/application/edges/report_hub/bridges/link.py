from zmena.application.edges.report_hub.records.link import LinkRecord


class LinkBridge:
    def __init__(self, fragment_bridge, evidence_bridge):
        self.fragment_bridge = fragment_bridge
        self.evidence_bridge = evidence_bridge

    def __repr__(self):
        return "LinkBridge(bridges=link,evidences,fragment)"

    def translate(self, link):
        left, right = link.fragments()
        evidences = link.evidence_bundle()

        return LinkRecord(
            score=link.score(),
            left=self.fragment_bridge.translate(left),
            right=self.fragment_bridge.translate(right),
            evidences=[self.evidence_bridge.translate(evidence) for evidence in evidences],
        )
