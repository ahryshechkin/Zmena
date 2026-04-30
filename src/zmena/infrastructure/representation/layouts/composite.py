from abc import ABC, abstractmethod


class CompositeReport(ABC):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        name = self.__class__.__name__.replace("Report", "")
        return f"Report(composite={name})"

    @abstractmethod
    def render(self):
        pass

    def title(self, idx, **metrics):
        desc = ", ".join(f"{key}={value}" for key, value in metrics.items())
        return f"{self.name} {idx}: {desc}"
