from dataclasses import dataclass


@dataclass(frozen=True)
class DropColumn:
    name: str
