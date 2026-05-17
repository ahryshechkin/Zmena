from zmena.domain.heuristics.heuristic import Heuristic
from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_kind import HeuristicKind


class PositionSimilarityHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicKind.POSITION_SIMILARITY)

    def evaluate(self, hypothesis):
        if hypothesis.has_same_position():
            return [Evidence(hypothesis, 1.0, 0.6, self.kind)]
        return []
