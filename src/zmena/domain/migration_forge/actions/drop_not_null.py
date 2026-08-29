from dataclasses import dataclass


@dataclass(frozen=True)
class DropNotNull:
    name: str
