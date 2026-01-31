from enum import Enum


class Tag(str, Enum):
    DELETE = "delete"
    EQUAL = "equal"
    INSERT = "insert"
    REPLACE = "replace"
    STUB = "stub"


class Color(str, Enum):
    GRAY = "\033[38;5;250m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"


class Side(str, Enum):
    LEFT = "L"
    RIGHT = "R"


class RuleId(str, Enum):
    NAME = "name"
    POSITION = "position"
    DELETE = "delete"
    INSERT = "insert"
    SIGNATURE = "signature"
