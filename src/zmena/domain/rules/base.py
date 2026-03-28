from abc import ABC, abstractmethod


class Rule(ABC):
    def __init__(self, label):
        self.label = label

    @abstractmethod
    def generate(self, bundle):
        pass
