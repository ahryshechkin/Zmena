from dataclasses import dataclass


@dataclass(frozen=True)
class DropNotNullStatement:
    name: str
