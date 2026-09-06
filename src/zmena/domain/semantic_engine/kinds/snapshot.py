from enum import StrEnum


class SnapshotKind(StrEnum):
    FRAGMENT = "fragment"
    LINK = "link"
    UNDEFINED = "undefined"
