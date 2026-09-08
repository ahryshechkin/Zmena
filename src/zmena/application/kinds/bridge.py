from enum import StrEnum


class BridgeKind(StrEnum):
    DECISION = "decision"
    FRAGMENT = "fragment"
    MATCH_BUNDLE = "match bundle"
    LINK = "link"
    STATE = "state"
    UNDEFINED = "undefined"
