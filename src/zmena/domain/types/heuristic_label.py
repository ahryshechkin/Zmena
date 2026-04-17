from enum import StrEnum


class HeuristicLabel(StrEnum):
    NAME_SIMILARITY = "name similarity"
    POSITION_SIMILARITY = "position similarity"
    SEGMENT_MISMATCH = "segment mismatch"
    SIGNATURE_SIMILARITY = "signature similarity"
