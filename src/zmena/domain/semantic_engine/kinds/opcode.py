from enum import StrEnum


class OpcodeKind(StrEnum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
    STUB = "stub"
    UNDEFINED = "undefined"
