from zmena.domain.lenses.lens import Lens
from zmena.domain.types.lens_kind import LensKind


class ColumnSwapLens(Lens):
    def __init__(self):
        super().__init__(LensKind.COLUMN_SWAP)

    def evaluate(self):
        return []
