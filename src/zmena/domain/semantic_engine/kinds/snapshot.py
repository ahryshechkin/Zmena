from enum import StrEnum


class SnapshotKind(StrEnum):
    COMPONENT = "component"
    DECISION = "decision"
    FRAGMENT = "fragment"
    HYPOTHESIS = "hypothesis"
    LINK = "link"
    UNDEFINED = "undefined"
