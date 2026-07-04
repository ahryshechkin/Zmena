from abc import ABC, abstractmethod


class Heuristic(ABC):
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Heuristic(kind={self.kind})"

    @abstractmethod
    def evaluate(self, hypothesis):
        pass
