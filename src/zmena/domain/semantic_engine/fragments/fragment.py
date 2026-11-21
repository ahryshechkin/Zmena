from zmena.domain.semantic_engine.kinds.opcode import OpcodeKind
from zmena.domain.semantic_engine.kinds.side import SideKind


class Fragment:
    def __init__(self, opcode, block, position, side, name, data_type, nullable):
        self.opcode = opcode
        self.block = block
        self.position = position
        self.side = side
        self.name = name
        self.data_type = data_type
        self.nullable = nullable

    def __repr__(self):
        return f"Fragment(opcode={self.opcode},name={self.name})"

    def same_name_as(self, other):
        return self.name == other.name

    def same_position_as(self, other):
        return self.position == other.position

    def same_signature_as(self, other):
        return (
            self.block == other.block
            and self.data_type == other.data_type
            and self.nullable == other.nullable
        )

    def same_name_but_different_block_as(self, other):
        return self.block != other.block and self.name == other.name

    def is_delete(self):
        return self.opcode == OpcodeKind.DELETE and self.side == SideKind.LEFT

    def is_insert(self):
        return self.opcode == OpcodeKind.INSERT and self.side == SideKind.RIGHT

    def is_replace(self):
        return self.opcode == OpcodeKind.REPLACE
