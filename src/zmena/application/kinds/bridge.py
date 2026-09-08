from enum import StrEnum


class BridgeKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    MATCH = "match"
    LINK = "link"
    STATE = "state"
    UNDEFINED = "undefined"
