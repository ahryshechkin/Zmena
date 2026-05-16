from zmena.domain.presets.rules import RulePreset


class HypothesisProposer:
    def __init__(self, bundle):
        self.bundle = bundle
        self.preset = RulePreset()

    def __repr__(self):
        return "HypothesisProposer(preset=rules)"

    def propose(self):
        hypotheses = []
        for rule in self.preset.default():
            hypotheses.extend(rule.generate(self.bundle))

        return hypotheses
