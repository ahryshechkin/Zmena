from enum import StrEnum


class RuleKind(StrEnum):
    DELETE = "delete"
    IMBALANCE = "imbalance"
    INSERT = "insert"
    NAME = "name"
    POSITION = "position"
    SIGNATURE = "signature"
