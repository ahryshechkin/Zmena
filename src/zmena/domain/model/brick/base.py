from zmena.domain.types.side import Side
from zmena.domain.types.tag import Tag


class Brick:
    def __init__(self, tag, side, segment, position, name, data_type, constraint):
        self.tag = tag
        self.side = side
        self.segment = segment
        self.position = position
        self.name = name
        self.data_type = data_type
        self.constraint = constraint

    def __str__(self):
        constraint = self.constraint or ""
        return (
            f"{self.tag.value:>7} | {self.side.value:>4} | "
            f"{self.segment:>8} | {self.position:>8} | "
            f"{self.name:<7} | {self.data_type:<13} | {constraint:>10} |"
        )

    def __repr__(self):
        return f"Brick(tag={self.tag.value},name={self.name})"

    def same_name_as(self, brick):
        return self.name == brick.name

    def same_position_as(self, brick):
        return self.position == brick.position

    def same_signature_as(self, brick):
        return (
            self.segment == brick.segment
            and self.data_type == brick.data_type
            and self.constraint == brick.constraint
        )

    def is_delete(self):
        return self.tag == Tag.DELETE and self.side == Side.LEFT

    def is_insert(self):
        return self.tag == Tag.INSERT and self.side == Side.RIGHT
