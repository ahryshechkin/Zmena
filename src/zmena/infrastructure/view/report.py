class Report:
    def __init__(self, desc, schema, rows):
        self.desc = desc
        self.schema = schema
        self.rows = rows

    def render(self):
        self.title()
        self.header()
        self.separator()
        self.body()
        self.separator()

    def title(self):
        prefix = f"\n#### {self.desc} "
        width = self.length() - len(prefix)
        print(f"{prefix}" + "#" * width)

    def header(self):
        row = " | ".join(f"{h:{a}{w}}" for h, a, w in self.schema)
        print(f"| {row} |")

    def separator(self):
        sep = "-+-".join("-" * int(w) for _, _, w in self.schema)
        print(f"+-{sep}-+")

    def body(self):
        for row in self.rows:
            print(f"| {row} |")

    def length(self):
        return sum(int(w) + 3 for _, _, w in self.schema) + 2
