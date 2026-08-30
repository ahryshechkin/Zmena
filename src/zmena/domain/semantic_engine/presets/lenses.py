from zmena.domain.semantic_engine.kinds.preset import PresetKind
from zmena.domain.semantic_engine.lenses.column_swap import ColumnSwapLens
from zmena.domain.semantic_engine.presets.preset import Preset


class LensPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.LENSES)
        self.column_swap = ColumnSwapLens()

    def default(self):
        return [self.column_swap]
