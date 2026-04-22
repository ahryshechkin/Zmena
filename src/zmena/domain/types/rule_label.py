from enum import StrEnum


class RuleLabel(StrEnum):
    DELETE = "delete"
    IMBALANCE = "imbalance"
    INSERT = "insert"
    NAME = "name"
    POSITION = "position"
    SIGNATURE = "signature"
