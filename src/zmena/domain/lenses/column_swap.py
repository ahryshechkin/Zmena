from zmena.domain.lenses.lens import Lens
from zmena.domain.types.lens_label import LensLabel


class ColumnSwapLens(Lens):
    def __init__(self):
        super().__init__(LensLabel.COLUMN_SWAP)

    def evaluate(self, link, context):
        pass
