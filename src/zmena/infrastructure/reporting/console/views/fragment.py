class FragmentView:
    def __init__(self, fragment):
        self.tag = fragment.tag
        self.block = fragment.block
        self.position = fragment.position
        self.side = fragment.side
        self.name = fragment.name
        self.data_type = fragment.data_type
        self.nullable = fragment.nullable

    def __str__(self):
        nullable = "" if self.nullable else "NOT NULL"
        return (
            f"{self.tag:>8} | {self.block:>8} | "
            f"{self.position:>8} | {self.side:>4} | "
            f"{self.name:<7} | {self.data_type:<13} | {nullable:>10}"
        )

    def caption(self):
        if self.tag == "Stub":
            return "Stub"
        return f"{self.name} ({self.side}:{self.position})"
