class DecisionView:
    def __init__(self, candidate_bundle, winner_bundle):
        self.candidate_bundle = candidate_bundle
        self.winner_bundle = winner_bundle

    def candidates(self):
        return self.candidate_bundle

    def winners(self):
        return self.winner_bundle

    def __repr__(self):
        return f"DecisionView(candidates={len(self.candidates())},winners={len(self.winners())})"
