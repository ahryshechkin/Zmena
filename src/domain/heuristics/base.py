from abc import ABC, abstractmethod


class Heuristic(ABC):
    @abstractmethod
    def score(self, link):
        pass
