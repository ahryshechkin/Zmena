from dataclasses import dataclass


@dataclass(frozen=True)
class SetNotNull:
    name: str
