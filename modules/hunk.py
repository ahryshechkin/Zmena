from constant import Tag


class Hunk:
    def __init__(self, opcode, left, right):
        self.opcode = Tag(opcode)
        self.left = left
        self.right = right


    def tag(self):
        return self.opcode


    def uid(self):
        return f"{self.left.uid()}{self.right.uid()}"


    def left_lineno(self, offset):
        if offset < self.left_range():
            return self.left.lineno(offset + 1)
        return ""


    def left_line(self, offset):
        if offset < self.left_range():
            return self.left.line(offset)
        return ""


    def left_range(self):
        return self.left.range()


    def right_lineno(self, offset):
        if offset < self.right_range():
            return self.right.lineno(offset + 1)
        return ""


    def right_line(self, offset):
        if offset < self.right_range():
            return self.right.line(offset)
        return ""


    def right_range(self):
        return self.right.range()


    def height(self):
        return max(self.left.range(), self.right.range())
