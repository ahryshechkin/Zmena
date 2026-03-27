from enum import StrEnum


class Tag(StrEnum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
    STUB = "stub"
