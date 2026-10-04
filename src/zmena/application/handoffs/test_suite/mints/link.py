from zmena.application.handoffs.test_suite.records.link import LinkRecord


class LinkMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "LinkMint(mints=link,fragment)"

    def issue(self, link):
        left, right = link.fragments()

        return LinkRecord(
            left=self.mint.issue(left),
            right=self.mint.issue(right),
        )
