from enum import StrEnum


class SnapshotKind(StrEnum):
    COMPONENT = "component"
    DECISION = "decision"
    FRAGMENT = "fragment"
    HYPOTHESIS = "hypothesis"
    LIGHTWEIGHT_LINK = "lightweight link"
    LINK = "link"
    UNDEFINED = "undefined"
