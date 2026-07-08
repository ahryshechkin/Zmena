from zmena.domain.semantic_engine.core.evidence import Evidence
from zmena.domain.semantic_engine.heuristics.heuristic import Heuristic
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind


class SignatureSimilarityHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicKind.SIGNATURE_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_signature():
            return [Evidence(hypothesis, 1.0, 1.0, self.kind)]
        return []
