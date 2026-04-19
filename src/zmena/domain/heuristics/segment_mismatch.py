from zmena.domain.model.evidence import Evidence
from zmena.domain.types.heuristic_label import HeuristicLabel

from .heuristic import Heuristic


class SegmentMismatchHeuristic(Heuristic):
    def __init__(self):
        super().__init__(HeuristicLabel.SEGMENT_MISMATCH)

    def evaluate(self, hypothesis):
        if hypothesis.has_segment_mismatch():
            return [Evidence(hypothesis, -1.0, 0.6, self.label)]
        return []
