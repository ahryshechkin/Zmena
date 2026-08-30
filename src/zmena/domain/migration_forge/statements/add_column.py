from dataclasses import dataclass


@dataclass(frozen=True)
class AddColumnStatement:
    name: str
    data_type: str
    nullable: bool
