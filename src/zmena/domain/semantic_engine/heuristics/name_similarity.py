from zmena.domain.semantic_engine.heuristics.heuristic import Heuristic
from zmena.domain.semantic_engine.model.evidence import Evidence
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind


class NameSimilarityHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicKind.NAME_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_name():
            return [Evidence(hypothesis, 1.0, 2.0, self.kind)]
        return []
