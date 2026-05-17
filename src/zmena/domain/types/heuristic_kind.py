from enum import StrEnum


class HeuristicKind(StrEnum):
    BLOCK_MISMATCH = "block mismatch"
    NAME_SIMILARITY = "name similarity"
    POSITION_SIMILARITY = "position similarity"
    SIGNATURE_SIMILARITY = "signature similarity"
