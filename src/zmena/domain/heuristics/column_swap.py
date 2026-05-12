from zmena.domain.heuristics.heuristic import Heuristic
from zmena.domain.types.heuristic_label import HeuristicLabel


class ColumnSwapHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.COLUMN_SWAP)

    def evaluate(self, link):
        pass
