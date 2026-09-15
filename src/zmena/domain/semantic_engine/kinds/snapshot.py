from enum import StrEnum


class SnapshotKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    HYPOTHESIS = "hypothesis"
    LINK = "link"
    UNDEFINED = "undefined"
