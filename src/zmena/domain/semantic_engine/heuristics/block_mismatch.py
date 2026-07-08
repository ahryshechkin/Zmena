from zmena.domain.semantic_engine.core.evidence import Evidence
from zmena.domain.semantic_engine.heuristics.heuristic import Heuristic
from zmena.domain.semantic_engine.types.heuristic_kind import HeuristicKind


class BlockMismatchHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicKind.BLOCK_MISMATCH)

    def evaluate(self, hypothesis):
        if hypothesis.has_block_mismatch():
            return [Evidence(hypothesis, -1.0, 1.2, self.kind)]
        return []
