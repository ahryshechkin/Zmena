from enum import StrEnum


class ProjectionKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    LINK = "link"
    UNDEFINED = "undefined"
