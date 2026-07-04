from abc import ABC, abstractmethod


class Rule(ABC):
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Rule(kind={self.kind})"

    @abstractmethod
    def generate(self, bundle):
        pass
