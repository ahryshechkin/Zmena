from zmena.infrastructure.reporting.console.views.link import LinkView


class LinkMint:
    def __init__(self, fragment_mint, evidence_mint):
        self.fragment_mint = fragment_mint
        self.evidence_mint = evidence_mint

    def __repr__(self):
        return "LinkMint(mints=link,evidence,fragment)"

    def issue(self, link):
        left, right = link.fragments()
        evidences = [self.evidence_mint.issue(evidence) for evidence in link.evidence_bundle()]

        return LinkView(
            link.score(), self.fragment_mint.issue(left), self.fragment_mint.issue(right), evidences
        )
