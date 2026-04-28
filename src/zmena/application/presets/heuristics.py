from zmena.domain.heuristics.name_similarity import NameSimilarityHeuristic
from zmena.domain.heuristics.position_similarity import PositionSimilarityHeuristic
from zmena.domain.heuristics.segment_mismatch import SegmentMismatchHeuristic
from zmena.domain.heuristics.signature_similarity import SignatureSimilarityHeuristic


class HeuristicPreset:
    def __init__(self):
        self.name_similarity = NameSimilarityHeuristic()
        self.position_similarity = PositionSimilarityHeuristic()
        self.segment_mismatch = SegmentMismatchHeuristic()
        self.signature_similarity = SignatureSimilarityHeuristic()

    def __repr__(self):
        return "Preset(type=heuristics)"

    def default(self):
        return [
            self.name_similarity,
            self.position_similarity,
            self.segment_mismatch,
            self.signature_similarity,
        ]
