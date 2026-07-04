from zmena.domain.semantic_engine.lenses.column_swap import ColumnSwapLens
from zmena.domain.semantic_engine.presets.preset import Preset
from zmena.domain.semantic_engine.types.preset_kind import PresetKind


class LensPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.LENSES)
        self.column_swap = ColumnSwapLens()

    def default(self):
        return [self.column_swap]
