from dataclasses import dataclass


@dataclass(frozen=True)
class AddColumn:
    name: str
    data_type: str
    nullable: bool
