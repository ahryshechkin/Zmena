from dataclasses import dataclass


@dataclass(frozen=True)
class AlterDataType:
    name: str
    old_data_type: str
    new_data_type: str
