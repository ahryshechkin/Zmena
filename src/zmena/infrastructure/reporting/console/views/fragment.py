class FragmentView:
    def __init__(self, tag, block, position, side, name, data_type, nullable):
        self.tag = tag
        self.block = block
        self.position = position
        self.side = side
        self.name = name
        self.data_type = data_type
        self.nullable = nullable

    def __str__(self):
        return (
            f"{self.tag:>8} | {self.block:>8} | {self.position:>8} | {self.side:>4} | "
            f"{self.name:<7} | {self.data_type:<13} | {self.nullable:>10}"
        )

    def __repr__(self):
        return f"FragmentView(tag={self.tag},name={self.name})"

    def caption(self):
        if self.tag == "stub":
            return "Stub"
        return f"{self.name} ({self.side}:{self.position})"
