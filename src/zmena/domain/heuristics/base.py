from abc import ABC, abstractmethod


class Heuristic(ABC):
    def __repr__(self):
        return f"Heuristic(type={self.__class__.__name__})"

    @abstractmethod
    def evaluate(self, hypothesis):
        pass
