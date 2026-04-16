from zmena.domain.heuristics.name import HeuristicName
from zmena.domain.heuristics.position import HeuristicPosition
from zmena.domain.heuristics.segment_mismatch import HeuristicSegmentMismatch
from zmena.domain.heuristics.signature import HeuristicSignature


class HeuristicRegistry:
    def __init__(self):
        self.name = HeuristicName()
        self.position = HeuristicPosition()
        self.segment_mismatch = HeuristicSegmentMismatch()
        self.signature = HeuristicSignature()

    def __repr__(self):
        return "Registry(type=heuristic)"

    def default_heuristics(self):
        return [
            self.name,
            self.position,
            self.segment_mismatch,
            self.signature,
        ]
