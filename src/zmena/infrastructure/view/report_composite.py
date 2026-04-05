from abc import ABC, abstractmethod


class ReportComposite(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def render(self):
        pass

    def title(self, idx, **metrics):
        desc = ", ".join(f"{key}={value}" for key, value in metrics.items())
        return f"{self.name} {idx}: {desc}"
