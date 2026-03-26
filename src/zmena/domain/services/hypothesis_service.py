class HypothesisService:
    def __init__(self, registry):
        self.registry = registry

    def propose(self, bundle):
        hypotheses = []
        for rule in self.registry.default_rules():
            hypotheses.extend(rule.generate(bundle))

        return hypotheses
