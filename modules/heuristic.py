from abc import ABC, abstractmethod


class Heuristic(ABC):
    @abstractmethod
    def score(self):
        pass


class HeuristicName(Heuristic):
    def score(self):
        return 10


class HeuristicPosition(Heuristic):
    def score(self):
        return 5
