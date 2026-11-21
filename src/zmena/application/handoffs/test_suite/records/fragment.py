from dataclasses import dataclass


@dataclass
class FragmentRecord:
    opcode: str
    block: str | None
    position: int | None
    side: str
    name: str | None
    data_type: str | None
    nullable: bool

    def __repr__(self):
        return f"FragmentRecord(opcode={self.tag},name={self.name})"
