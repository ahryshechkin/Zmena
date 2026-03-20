from abc import ABC, abstractmethod


class Heuristic(ABC):
    @abstractmethod
    def evaluate(self, hypothesis):
        pass
