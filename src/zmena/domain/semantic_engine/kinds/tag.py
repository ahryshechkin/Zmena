from enum import StrEnum


class TagKind(StrEnum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
    STUB = "stub"
