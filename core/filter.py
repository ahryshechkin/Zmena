class Filter:
    def __init__(self, bricks):
        self.bricks = bricks


    def by_tag(self, tag):
        result = [brick for brick in self.bricks if brick.tag == tag]
        return Filter(result)


    def by_side(self, side):
        result = [brick for brick in self.bricks if brick.side == side]
        return Filter(result)


    def result(self):
        return self.bricks
