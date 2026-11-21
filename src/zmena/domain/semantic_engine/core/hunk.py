from zmena.domain.semantic_engine.kinds.opcode import OpcodeKind


class Hunk:
    def __init__(self, opcode, left, right):
        self.opcode = OpcodeKind(opcode)
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Hunk(opcode={self.opcode})"

    def kind(self):
        return self.opcode

    def fingerprint(self):
        return f"{self.left.fingerprint()}{self.right.fingerprint()}"

    def left_line(self, offset):
        if offset < self.left_range():
            return self.left.line(offset)
        return ""

    def left_lineno(self, offset):
        if offset < self.left_range():
            return self.left.lineno(offset + 1)
        return ""

    def left_range(self):
        return self.left.range()

    def right_line(self, offset):
        if offset < self.right_range():
            return self.right.line(offset)
        return ""

    def right_lineno(self, offset):
        if offset < self.right_range():
            return self.right.lineno(offset + 1)
        return ""

    def right_range(self):
        return self.right.range()

    def height(self):
        return max(self.left.range(), self.right.range())
