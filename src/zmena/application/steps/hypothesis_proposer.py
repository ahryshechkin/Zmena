class HypothesisProposer:
    def __init__(self, rules):
        self.rules = rules

    def __repr__(self):
        return "HypothesisProposer(preset=rules)"

    def propose(self, bundle):
        hypotheses = []
        for rule in self.rules:
            hypotheses.extend(rule.generate(bundle))

        return hypotheses
