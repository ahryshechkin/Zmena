from abc import ABC, abstractmethod


class Lens(ABC):
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"Lens(label={self.label})"

    @abstractmethod
    def evaluate(self, link, context):
        pass
