from enum import StrEnum


class SnapshotKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    LINK = "link"
    UNDEFINED = "undefined"
