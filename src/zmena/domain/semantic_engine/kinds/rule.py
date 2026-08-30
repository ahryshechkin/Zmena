from enum import StrEnum


class RuleKind(StrEnum):
    DELETE = "delete"
    HUNK_SURPLUS_LEFT = "hunk surplus left"
    HUNK_SURPLUS_RIGHT = "hunk surplus right"
    INSERT = "insert"
    NAME = "name"
    POSITION = "position"
    SIGNATURE = "signature"
