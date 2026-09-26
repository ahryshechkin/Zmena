from dataclasses import dataclass


@dataclass
class FragmentSnapshot:
    tag: str
    block: str
    position: str
    side: str
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return f"FragmentSnapshot(tag={self.tag},name={self.name})"
