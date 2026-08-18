from abc import ABC, abstractmethod


class Criteria(ABC):
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Criteria(kind={self.kind})"

    @abstractmethod
    def apply(self, paths):
        pass
