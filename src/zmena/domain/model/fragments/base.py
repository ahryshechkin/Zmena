from zmena.domain.types.side import Side
from zmena.domain.types.tag import Tag


class Fragment:
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
            f"{self.tag.value:>8} | {self.side.value:>4} | "
            f"{self.segment:>8} | {self.position:>8} | "
            f"{self.name:<7} | {self.data_type:<13} | {constraint:>10}"
        )

    def __repr__(self):
        return f"Fragment(tag={self.tag.value},name={self.name})"

    def same_name_as(self, other):
        return self.name == other.name

    def same_position_as(self, other):
        return self.position == other.position

    def same_signature_as(self, other):
        return (
            self.segment == other.segment
            and self.data_type == other.data_type
            and self.constraint == other.constraint
        )

    def same_name_but_different_segment_as(self, other):
        return self.segment != other.segment and self.name == other.name

    def is_delete(self):
        return self.tag == Tag.DELETE and self.side == Side.LEFT

    def is_insert(self):
        return self.tag == Tag.INSERT and self.side == Side.RIGHT
