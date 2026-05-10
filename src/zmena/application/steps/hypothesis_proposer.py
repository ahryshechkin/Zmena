from zmena.domain.presets.rules import RulePreset


class HypothesisProposer:
    def __init__(self):
        self.preset = RulePreset()

    def __repr__(self):
        return "HypothesisProposer(preset=rules)"

    def propose(self, bundle):
        hypotheses = []
        for rule in self.preset.default():
            hypotheses.extend(rule.generate(bundle))

        return hypotheses
