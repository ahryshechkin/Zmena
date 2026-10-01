from dataclasses import dataclass


@dataclass
class FragmentRecord:
    tag: str
    block: str
    position: str
    side: str
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return f"FragmentRecord(tag={self.tag},name={self.name})"
