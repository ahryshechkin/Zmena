from modules.constant import Tag

from .base import Brick


class BrickStub(Brick):
    def __init__(self, side):
        super().__init__(Tag.STUB, side, "", "", "", "", None)
