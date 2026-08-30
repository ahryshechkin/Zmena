from dataclasses import dataclass


@dataclass(frozen=True)
class RenameColumnStatement:
    old_name: str
    new_name: str
