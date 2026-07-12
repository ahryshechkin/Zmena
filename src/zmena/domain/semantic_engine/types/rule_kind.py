from enum import StrEnum


class RuleKind(StrEnum):
    DELETE = "delete"
    IMBALANCE = "imbalance"
    INSERT = "insert"
    HUNK_SURPLUS_LEFT = "hunk surplus left"
    NAME = "name"
    POSITION = "position"
    SIGNATURE = "signature"
