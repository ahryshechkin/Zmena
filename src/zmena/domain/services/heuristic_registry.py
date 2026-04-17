from zmena.domain.heuristics.name_similarity import HeuristicNameSimilarity
from zmena.domain.heuristics.position_similarity import HeuristicPositionSimilarity
from zmena.domain.heuristics.segment_mismatch import HeuristicSegmentMismatch
from zmena.domain.heuristics.signature_similarity import HeuristicSignatureSimilarity


class HeuristicRegistry:
    def __init__(self):
        self.name_similarity = HeuristicNameSimilarity()
        self.position_similarity = HeuristicPositionSimilarity()
        self.segment_mismatch = HeuristicSegmentMismatch()
        self.signature_similarity = HeuristicSignatureSimilarity()

    def __repr__(self):
        return "Registry(type=heuristic)"

    def default_heuristics(self):
        return [
            self.name_similarity,
            self.position_similarity,
            self.segment_mismatch,
            self.signature_similarity,
        ]
