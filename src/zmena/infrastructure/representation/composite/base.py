from abc import ABC, abstractmethod


class CompositeReport(ABC):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Report(composite={self.__class__.__name__.replace('Report', '')})"

    @abstractmethod
    def render(self):
        pass

    def title(self, idx, **metrics):
        desc = ", ".join(f"{key}={value}" for key, value in metrics.items())
        return f"{self.name} {idx}: {desc}"
