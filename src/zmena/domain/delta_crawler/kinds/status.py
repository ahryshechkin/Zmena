from enum import StrEnum


class StatusKind(StrEnum):
    ADDED = "A"
    DELETED = "D"
    MODIFIED = "M"
    UNDEFINED = "undefined"
