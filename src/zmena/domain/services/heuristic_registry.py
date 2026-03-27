from zmena.domain.heuristics.compatibility import HeuristicCompatibility
from zmena.domain.heuristics.name import HeuristicName
from zmena.domain.heuristics.position import HeuristicPosition
from zmena.domain.heuristics.signature import HeuristicSignature


class HeuristicRegistry:
    def __init__(self):
        self.compatibility = HeuristicCompatibility()
        self.name = HeuristicName()
        self.position = HeuristicPosition()
        self.signature = HeuristicSignature()

    def default_heuristics(self):
        return [
            self.compatibility,
            self.name,
            self.position,
            self.signature,
        ]
