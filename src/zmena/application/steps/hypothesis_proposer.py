class HypothesisProposer:
    def __init__(self, registry):
        self.registry = registry

    def __repr__(self):
        return "HypothesisProposer(registry=rule)"

    def propose(self, bundle):
        hypotheses = []
        for rule in self.registry.default_rules():
            hypotheses.extend(rule.generate(bundle))

        return hypotheses
