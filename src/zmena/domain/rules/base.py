from abc import ABC, abstractmethod


class Rule(ABC):
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"Rule(label={self.label})"

    @abstractmethod
    def generate(self, bundle):
        pass
