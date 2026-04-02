class Report:
    def __init__(self, schema):
        self.schema = schema

    def render(self):
        self.title()
        self.header()
        self.separator()
        self.body()

    def title(self):
        pass

    def header(self):
        print(" | ".join(f"{h:{a}{w}}" for h, a, w in self.schema))

    def separator(self):
        pass

    def body(self):
        pass
