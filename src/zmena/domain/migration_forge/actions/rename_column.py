from dataclasses import dataclass


@dataclass(frozen=True)
class RenameColumn:
    old_name: str
    new_name: str
