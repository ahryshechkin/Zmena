from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .heuristic import Heuristic


class SignatureSimilarityHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.SIGNATURE_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_signature():
            return [Evidence(hypothesis, 1.0, 0.5, self.label)]
        return []
