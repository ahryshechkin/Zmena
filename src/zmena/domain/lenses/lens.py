from abc import ABC, abstractmethod


class Lens(ABC):
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Lens(kind={self.kind})"

    @abstractmethod
    def evaluate(self, link, context):
        pass
