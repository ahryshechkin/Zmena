from enum import StrEnum


class RuleLabel(StrEnum):
    NAME = "name"
    POSITION = "position"
    DELETE = "delete"
    INSERT = "insert"
    SIGNATURE = "signature"
    OVERFLOW = "overflow"
