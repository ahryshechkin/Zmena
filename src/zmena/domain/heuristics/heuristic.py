from abc import ABC, abstractmethod


class Heuristic(ABC):
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"Heuristic(label={self.label})"

    @abstractmethod
    def evaluate(self, hypothesis):
        pass
