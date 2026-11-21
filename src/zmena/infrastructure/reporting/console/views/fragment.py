class FragmentView:
    def __init__(self, opcode, block, position, side, name, data_type, constraint):
        self.opcode = opcode
        self.block = block
        self.position = position
        self.side = side
        self.name = name
        self.data_type = data_type
        self.constraint = constraint

    def __str__(self):
        return (
            f"{self.opcode:>8} | {self.block:>8} | {self.position:>8} | {self.side:>4} | "
            f"{self.name:<7} | {self.data_type:<13} | {self.constraint:>10}"
        )

    def __repr__(self):
        return f"FragmentView(opcode={self.opcode},name={self.name})"

    def caption(self):
        if self.opcode == "stub":
            return "Stub"
        return f"{self.name} ({self.side}:{self.position})"
