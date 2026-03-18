from enum import StrEnum


class Tag(StrEnum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
    STUB = "stub"


class Color(StrEnum):
    GRAY = "\033[38;5;250m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"


class Side(StrEnum):
    LEFT = "L"
    RIGHT = "R"


class RuleId(StrEnum):
    NAME = "name"
    POSITION = "position"
    DELETE = "delete"
    INSERT = "insert"
    SIGNATURE = "signature"
    OVERFLOW = "overflow"
