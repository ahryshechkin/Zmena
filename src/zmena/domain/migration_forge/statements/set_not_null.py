from dataclasses import dataclass


@dataclass(frozen=True)
class SetNotNullStatement:
    name: str
