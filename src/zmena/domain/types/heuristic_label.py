from enum import StrEnum


class HeuristicLabel(StrEnum):
    COMPATIBILITY = "segment mismatch"
    NAME = "name"
    POSITION = "position"
    SIGNATURE = "signature"
