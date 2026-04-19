class BasicReport:
    def __init__(self, name, schema, rows):
        self.name = name
        self.schema = schema
        self.rows = rows

    def __repr__(self):
        name = self.__class__.__name__.replace("Report", "")
        return f"Report(basic={name})"

    def render(self):
        self.title()
        self.header()
        self.separator()
        self.body()
        self.separator()

    def title(self):
        prefix = f"#### {self.name} "
        width = self.length() - len(prefix)
        print(f"\n{prefix}" + "#" * width)

    def header(self):
        cols = " | ".join(f"{h:{a}{w}}" for h, a, w in self.schema)
        print(f"| {cols} |")

    def separator(self):
        sep = "-+-".join("-" * int(w) for _, _, w in self.schema)
        print(f"+-{sep}-+")

    def body(self):
        for row in self.rows:
            print(f"| {row} |")

    def length(self):
        return sum(int(w) + 3 for _, _, w in self.schema) + 1
