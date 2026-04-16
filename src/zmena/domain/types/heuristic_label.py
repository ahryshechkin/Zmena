from enum import StrEnum


class HeuristicLabel(StrEnum):
    NAME = "name"
    POSITION = "position"
    SEGMENT_MISMATCH = "segment mismatch"
    SIGNATURE = "signature"
