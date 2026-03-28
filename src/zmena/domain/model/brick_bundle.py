from zmena.domain.types.side import Side


class BrickBundle:
    def __init__(self, bricks):
        self.bricks = bricks

    def __repr__(self):
        return f"BrickBundle(bricks={len(self.bricks)})"

    def left(self):
        return [b for b in self.bricks if b.side == Side.LEFT]

    def right(self):
        return [b for b in self.bricks if b.side == Side.RIGHT]
