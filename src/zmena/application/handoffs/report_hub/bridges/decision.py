from zmena.infrastructure.reporting.console.views.decision import DecisionView


class DecisionMint:
    def __init__(self, mint):
        self.mint = mint

    def __repr__(self):
        return "DecisionMint(mints=decision,link,fragment)"

    def issue(self, decision):
        candidate_bundle = [self.mint.issue(link) for link in decision.candidates()]
        winner_bundle = [self.mint.issue(link) for link in decision.winners()]

        return DecisionView(candidate_bundle, winner_bundle)
