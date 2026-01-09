from modules.coordinate import Coordinate


class Hunk:
    def __init__(self, tag, left, right):
        self.tag = tag
        self.left = left
        self.right = right


    def left_lineno(self, index):
        return self.left.lineno(index + 1)


    def left_line(self, index):
        return self.left.line(index)


    def left_range(self):
        return self.left.range()


    def right_lineno(self, index):
        return self.right.lineno(index + 1)


    def right_line(self, index):
        return self.right.line(index)


    def right_range(self):
        return self.right.range()


    def height(self):
        return max(self.left.range(), self.right.range())


    def index(self):
        return f"{self.left.index()}{self.right.index()}"


    def left_coordinate(self, index):
        return Coordinate(self.index(), self.left.lineno(index))