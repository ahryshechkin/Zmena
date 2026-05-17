from zmena.domain.heuristics.block_mismatch import BlockMismatchHeuristic
from zmena.domain.heuristics.name_similarity import NameSimilarityHeuristic
from zmena.domain.heuristics.position_similarity import PositionSimilarityHeuristic
from zmena.domain.heuristics.signature_similarity import SignatureSimilarityHeuristic
from zmena.domain.presets.preset import Preset
from zmena.domain.types.preset_kind import PresetKind


class HeuristicPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.HEURISTICS)
        self.block_mismatch = BlockMismatchHeuristic()
        self.name_similarity = NameSimilarityHeuristic()
        self.position_similarity = PositionSimilarityHeuristic()
        self.signature_similarity = SignatureSimilarityHeuristic()

    def __repr__(self):
        return f"Preset(kind={self.kind})"

    def default(self):
        return [
            self.block_mismatch,
            self.name_similarity,
            self.position_similarity,
            self.signature_similarity,
        ]
