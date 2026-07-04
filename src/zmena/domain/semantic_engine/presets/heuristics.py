from zmena.domain.semantic_engine.heuristics.block_mismatch import BlockMismatchHeuristic
from zmena.domain.semantic_engine.heuristics.name_similarity import NameSimilarityHeuristic
from zmena.domain.semantic_engine.heuristics.position_similarity import PositionSimilarityHeuristic
from zmena.domain.semantic_engine.heuristics.signature_similarity import (
    SignatureSimilarityHeuristic,
)
from zmena.domain.semantic_engine.presets.preset import Preset
from zmena.domain.semantic_engine.types.preset_kind import PresetKind


class HeuristicPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.HEURISTICS)
        self.block_mismatch = BlockMismatchHeuristic()
        self.name_similarity = NameSimilarityHeuristic()
        self.position_similarity = PositionSimilarityHeuristic()
        self.signature_similarity = SignatureSimilarityHeuristic()

    def default(self):
        return [
            self.block_mismatch,
            self.name_similarity,
            self.position_similarity,
            self.signature_similarity,
        ]
