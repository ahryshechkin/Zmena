from zmena.domain.services.constant import Side


class BrickBundle:
    def __init__(self, bricks):
        self.bricks = bricks

    def left(self):
        return [b for b in self.bricks if b.side == Side.LEFT]

    def right(self):
        return [b for b in self.bricks if b.side == Side.RIGHT]
