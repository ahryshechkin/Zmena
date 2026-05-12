from enum import StrEnum


class HeuristicLabel(StrEnum):
    BLOCK_MISMATCH = "block mismatch"
    COLUMN_SWAP = "column swap"
    NAME_SIMILARITY = "name similarity"
    POSITION_SIMILARITY = "position similarity"
    SIGNATURE_SIMILARITY = "signature similarity"
