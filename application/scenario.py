from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    before: list[str]
    after: list[str]