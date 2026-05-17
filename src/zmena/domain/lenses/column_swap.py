from zmena.domain.lenses.lens import Lens
from zmena.domain.types.heuristic_label import HeuristicLabel


class ColumnSwapLens(Lens):
    def __init__(self):
        super().__init__(HeuristicLabel.COLUMN_SWAP)

    def evaluate(self, link, context):
        pass
