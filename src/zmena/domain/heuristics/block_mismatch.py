from zmena.domain.heuristics.heuristic import Heuristic
from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel


class BlockMismatchHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.BLOCK_MISMATCH)

    def evaluate(self, hypothesis):
        if hypothesis.has_block_mismatch():
            return [Evidence(hypothesis, -1.0, 1.2, self.label)]
        return []
