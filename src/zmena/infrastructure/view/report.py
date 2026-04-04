from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, schema):
        self.schema = schema

    def render(self, alias=None):
        self.title(alias)
        self.header()
        self.separator()
        self.body()
        self.separator()

    @abstractmethod
    def title(self, alias):
        pass

    def header(self):
        row = " | ".join(f"{h:{a}{w}}" for h, a, w in self.schema)
        print(f"| {row} |")

    def separator(self):
        sep = "-+-".join("-" * int(w) for _, _, w in self.schema)
        print(f"+-{sep}-+")

    @abstractmethod
    def body(self):
        pass

    def length(self):
        return sum(int(w) + 3 for _, _, w in self.schema) + 2
