from enum import StrEnum


class ProjectionKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    MATCH = "match"
    LINK = "link"
    STATE = "state"
    UNDEFINED = "undefined"
