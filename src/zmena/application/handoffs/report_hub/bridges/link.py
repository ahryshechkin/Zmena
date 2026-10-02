from zmena.application.handoffs.report_hub.records.link import LinkRecord


class LinkBridge:
    def __init__(self, fragment_mint, evidence_bridge):
        self.fragment_mint = fragment_mint
        self.evidence_bridge = evidence_bridge

    def __repr__(self):
        return "LinkBridge(bridges=link,fragment,evidences)"

    def translate(self, link):
        left, right = link.fragments()
        evidences = [
            self.evidence_bridge.translate(evidence) for evidence in link.evidence_bundle()
        ]

        return LinkRecord(
            score=link.score(),
            left=self.fragment_mint.issue(left),
            right=self.fragment_mint.issue(right),
            evidences=evidences,
        )
